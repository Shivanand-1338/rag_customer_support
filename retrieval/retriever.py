from config import TOP_K

def get_retriever(db):
    return db.as_retriever(search_kwargs={"k": TOP_K})


def retrieve_docs(retriever, query):
    return retriever.invoke(query)   # ✅ FIXED