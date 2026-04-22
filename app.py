from ingestion.loader import load_pdf
from ingestion.chunking import split_documents
from ingestion.embed_store import create_vector_store, load_vector_store
from retrieval.retriever import get_retriever
from graph.workflow import run_workflow
from utils.helpers import print_response
import os

PDF_PATH = "data/knowledge_base.pdf"


def setup():
    if not os.path.exists("chroma_db"):
        print("📄 Loading PDF...")
        docs = load_pdf(PDF_PATH)

        print("✂️ Chunking...")
        chunks = split_documents(docs)

        print("🧠 Creating embeddings...")
        db = create_vector_store(chunks)
    else:
        print("📦 Loading existing DB...")
        db = load_vector_store()

    return db


def main():
    db = setup()
    retriever = get_retriever(db)

    print("\n🤖 Customer Support Assistant Ready!\n")

    while True:
        query = input("Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        state = run_workflow(query, retriever)
        print_response(state)


if __name__ == "__main__":
    main()