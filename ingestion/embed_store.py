from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import PERSIST_DIR, EMBEDDING_MODEL


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )

    return db   # ❌ remove db.persist()


def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )