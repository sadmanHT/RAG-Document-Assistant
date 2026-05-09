import json
import yaml
import numpy as np
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder

# --- Module-Level Initialization ---

# 1. Load Configurations
config_path = Path("config/prompts.yaml")
try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    config = {}

DEFAULT_TOP_K_RETRIEVAL = config.get("retrieval", {}).get("top_k_retrieval", 20)
DEFAULT_TOP_K_FINAL = config.get("retrieval", {}).get("top_k_final", 5)

# 2. Initialize Vectorstore
persist_dir = "vectorstore/"
print("Loading Embedding Model & Vectorstore...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(
    collection_name="k8s_docs",
    embedding_function=embeddings,
    persist_directory=persist_dir
)

# 3. Initialize BM25
chunks_json_path = Path("data/processed/chunks.json")
chunks_data = []
bm25 = None

if chunks_json_path.exists():
    print("Loading Chunks & building BM25 Index...")
    with open(chunks_json_path, "r", encoding="utf-8") as f:
        chunks_data = json.load(f)
    
    # Tokenize text by splitting by whitespace
    tokenized_corpus = [chunk["text"].split() for chunk in chunks_data]
    bm25 = BM25Okapi(tokenized_corpus)
else:
    print(f"Warning: {chunks_json_path} not found. BM25 will not work properly.")

# 4. Initialize CrossEncoder
print("Loading CrossEncoder model...")
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
print("--- Module Initialized Successfully ---")


def hybrid_retrieve(query: str, top_k_retrieval: int = DEFAULT_TOP_K_RETRIEVAL):
    """
    Runs vector search and BM25 search, then merges results using Reciprocal Rank Fusion (RRF).
    """
    
    # Run Vector Similarity Search
    vector_results = vectorstore.similarity_search(query, k=top_k_retrieval)
    vector_docs = [
        {"text": doc.page_content, "metadata": doc.metadata} 
        for doc in vector_results
    ]
    
    # Run BM25 Search
    bm25_docs = []
    if bm25 is not None:
        tokenized_query = query.split()
        bm25_scores = bm25.get_scores(tokenized_query)
        # Get indices of the top top_k_retrieval scores
        top_n_indices = np.argsort(bm25_scores)[::-1][:top_k_retrieval]
        
        bm25_docs = [
            {"text": chunks_data[i]["text"], "metadata": chunks_data[i]["metadata"]}
            for i in top_n_indices
        ]

    # Merge using Reciprocal Rank Fusion (RRF)
    # RRF formula: 1 / (rank + 60)
    rrf_scores = {}
    merged_docs = {}

    def get_doc_id(doc):
        # Create a unique ID using source and chunk_index to identify duplicates
        return f"{doc['metadata'].get('source', '')}_{doc['metadata'].get('chunk_index', '')}"

    # Score Vector Docs
    for rank, doc in enumerate(vector_docs):
        doc_id = get_doc_id(doc)
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (rank + 60.0))
        merged_docs[doc_id] = doc
        
    # Score BM25 Docs
    for rank, doc in enumerate(bm25_docs):
        doc_id = get_doc_id(doc)
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (rank + 60.0))
        merged_docs[doc_id] = doc

    # Create final sorted list
    final_candidates = []
    for doc_id, doc in merged_docs.items():
        doc_copy = doc.copy()
        doc_copy["rrf_score"] = rrf_scores[doc_id]
        final_candidates.append(doc_copy)

    # Sort descending by RRF score
    final_candidates.sort(key=lambda x: x["rrf_score"], reverse=True)
    
    # Return top_k_retrieval amount from the merged list
    return final_candidates[:top_k_retrieval]


def rerank(query: str, candidates: list, top_k_final: int = DEFAULT_TOP_K_FINAL):
    """
    Reranks candidate chunks using a CrossEncoder.
    """
    if not candidates:
        return []

    # Build input pairs: (query, candidate_text)
    pairs = [[query, cand["text"]] for cand in candidates]
    
    # Generate scores with the CrossEncoder model
    scores = cross_encoder.predict(pairs)
    
    # Attach scores to the candidate dictionaries
    for i, cand in enumerate(candidates):
        cand["cross_encoder_score"] = float(scores[i])
        
    # Sort descending by cross_encoder_score
    candidates.sort(key=lambda x: x["cross_encoder_score"], reverse=True)
    
    return candidates[:top_k_final]


def retrieve_and_rerank(query: str, top_k_retrieval: int = DEFAULT_TOP_K_RETRIEVAL, top_k_final: int = DEFAULT_TOP_K_FINAL):
    """
    Performs hybrid retrieval followed by cross-encoder reranking.
    """
    candidates = hybrid_retrieve(query, top_k_retrieval=top_k_retrieval)
    final_docs = rerank(query, candidates, top_k_final=top_k_final)
    return final_docs


if __name__ == "__main__":
    test_query = "what is a kubernetes namespace"
    print(f"\n--- Testing retrieve_and_rerank ---")
    print(f"Query: '{test_query}'\n")
    
    results = retrieve_and_rerank(test_query)
    
    for i, res in enumerate(results, 1):
        source = res["metadata"].get("source", "Unknown")
        chunk_idx = res["metadata"].get("chunk_index", "Unknown")
        ce_score = res.get("cross_encoder_score", 0.0)
        rrf_score = res.get("rrf_score", 0.0)
        preview = res["text"][:150].replace('\n', ' ')
        
        print(f"Rank {i} | Source: {source} (Chunk {chunk_idx}) | CE Score: {ce_score:.4f} | RRF Score: {rrf_score:.4f}")
        print(f"Preview : {preview}...\n")
