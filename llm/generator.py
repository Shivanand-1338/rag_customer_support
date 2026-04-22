from langchain_groq import ChatGroq
from config import GROQ_API_KEY

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a professional customer support assistant.

Instructions:
- Answer ONLY from the context
- Provide COMPLETE and DETAILED answers
- If rules/policies → use bullet points
- Do NOT truncate
- If answer not found → say "I don't know"

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    # confidence logic
    confidence = 0.9 if context.strip() else 0.3

    return response.content, confidence