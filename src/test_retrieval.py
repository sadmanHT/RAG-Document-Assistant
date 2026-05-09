from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def main():
    persist_dir = "vectorstore/"
    
    # Verify the vector store directory exists
    if not Path(persist_dir).exists():
        print(f"Error: Vectorstore directory '{persist_dir}' not found.")
        return

    print("Initializing embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print(f"Loading Chroma vector store from {persist_dir}...")
    vectorstore = Chroma(
        collection_name="k8s_docs",
        embedding_function=embeddings,
        persist_directory=persist_dir
    )

    query = "how does kubernetes schedule pods"
    print(f"\nQuery: '{query}'")
    
    # Run similarity search
    results = vectorstore.similarity_search(query, k=3)

    print(f"\n--- Top {len(results)} Results ---")
    for i, doc in enumerate(results, 1):
        source = doc.metadata.get("source", "Unknown")
        chunk_index = doc.metadata.get("chunk_index", "Unknown")
        # Format the content preview to remove excessive newlines
        content_preview = doc.page_content[:200].replace('\n', ' ')
        
        print(f"\nResult {i}:")
        print(f"Source: {source} (Chunk {chunk_index})")
        print(f"Content preview: {content_preview}...")

if __name__ == "__main__":
    main()
