import json
import yaml
from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def main():
    # 7. Read chunk_size and chunk_overlap from config/prompts.yaml using the pyyaml library
    config_path = Path("config/prompts.yaml")
    if not config_path.exists():
        print(f"Error: Configuration file not found at {config_path}")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    chunk_size = config.get("chunking", {}).get("chunk_size", 600)
    chunk_overlap = config.get("chunking", {}).get("chunk_overlap", 100)

    # Handle the case where data/raw/ is empty with a clear error message
    raw_dir = Path("data/raw")
    if not raw_dir.exists() or not any(raw_dir.glob("*.md")):
        print(f"Error: The directory {raw_dir} is empty or does not contain any .md files. Please run download_docs.py first.")
        return

    # 1. Load all .md files and attach metadata with the key 'source' set to the filename
    md_files = list(raw_dir.glob("*.md"))
    documents = []

    print("Loading documents...")
    for file_path in md_files:
        loader = UnstructuredMarkdownLoader(str(file_path))
        docs = loader.load()
        for doc in docs:
            # Set source to just the filename (e.g., pods.md)
            doc.metadata["source"] = file_path.name
            documents.append(doc)

    loaded_doc_count = len(documents)

    # 2. Split documents using RecursiveCharacterTextSplitter
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    chunks = text_splitter.split_documents(documents)

    # Add 'chunk_index' to each chunk's metadata
    source_chunk_counts = {}
    for chunk in chunks:
        source_name = chunk.metadata["source"]
        # Initialize count for the source if not exists
        idx = source_chunk_counts.get(source_name, 0)
        chunk.metadata["chunk_index"] = idx
        source_chunk_counts[source_name] = idx + 1

    # 5. Save the raw chunk texts and their metadata to a JSON file
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    chunks_json_path = processed_dir / "chunks.json"

    print(f"Saving {len(chunks)} chunks to {chunks_json_path}...")
    chunks_data = [
        {"text": chunk.page_content, "metadata": chunk.metadata}
        for chunk in chunks
    ]
    
    with open(chunks_json_path, "w", encoding="utf-8") as f:
        json.dump(chunks_data, f, indent=4)

    # 3. Generate embeddings using HuggingFaceEmbeddings
    print("Initializing embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Store chunks and embeddings in a ChromaDB vector store
    persist_dir = "vectorstore/"
    print(f"Building Chroma vector store at {persist_dir}...")
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir,
        collection_name="k8s_docs"
    )

    # 6. Print summary
    print("\n--- INGESTION SUMMARY ---")
    print(f"Total .md files loaded: {len(md_files)}")
    print(f"Total documents loaded: {loaded_doc_count}")
    print(f"Total chunks created: {len(chunks)}")
    print(f"Vectorstore saved successfully to: '{persist_dir}' with collection 'k8s_docs'.")
    print(f"Chunks JSON saved to: {chunks_json_path}")

# 8. Uses a main() function and runs it when the script is called directly
if __name__ == "__main__":
    main()
