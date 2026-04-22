import streamlit as st
from ingestion.embed_store import load_vector_store
from retrieval.retriever import get_retriever
from graph.workflow import run_workflow

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="RAG Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 RAG-Based Customer Support Assistant")
st.markdown("Ask questions from your PDF knowledge base")

# -----------------------------
# Load DB (cached)
# -----------------------------
@st.cache_resource
def load_system():
    db = load_vector_store()
    retriever = get_retriever(db)
    return retriever

retriever = load_system()

# -----------------------------
# Session State
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# User Input
# -----------------------------
query = st.chat_input("Ask your question...")

if query:
    # Add user message
    st.session_state.chat_history.append(("user", query))

    # Run workflow
    state = run_workflow(query, retriever)

    answer = state["answer"]
    confidence = state["confidence"]

    # Add bot response
    st.session_state.chat_history.append(("bot", answer, confidence))

# -----------------------------
# Display Chat
# -----------------------------
for msg in st.session_state.chat_history:
    if msg[0] == "user":
        with st.chat_message("user"):
            st.write(msg[1])
    else:
        with st.chat_message("assistant"):
            st.write(msg[1])
            st.caption(f"Confidence: {msg[2]:.2f}")

# -----------------------------
# Sidebar Info
# -----------------------------
st.sidebar.title("ℹ️ System Info")
st.sidebar.markdown("""
**Features:**
- RAG (Retrieval-Augmented Generation)
- ChromaDB Vector Store
- LangGraph Workflow
- Groq LLM Integration
- Human-in-the-Loop (HITL)

**Tips:**
- Ask specific questions
- Try policy-related queries
""")