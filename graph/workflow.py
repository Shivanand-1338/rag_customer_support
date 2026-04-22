from typing import TypedDict
from retrieval.retriever import retrieve_docs
from llm.generator import generate_answer
from hitl.human_loop import escalate_to_human
from config import CONFIDENCE_THRESHOLD

class GraphState(TypedDict):
    query: str
    docs: list
    answer: str
    confidence: float
    escalate: bool


def process_node(state, retriever):
    docs = retrieve_docs(retriever, state["query"])

    answer, confidence = generate_answer(state["query"], docs)

    escalate = False
    if confidence < CONFIDENCE_THRESHOLD or len(docs) == 0:
        escalate = True

    return {
        "docs": docs,
        "answer": answer,
        "confidence": confidence,
        "escalate": escalate
    }


def hitl_node(state):
    human_answer = escalate_to_human(state["query"])
    return {
        "answer": human_answer,
        "confidence": 1.0
    }


def run_workflow(query, retriever):
    state = {
        "query": query,
        "docs": [],
        "answer": "",
        "confidence": 0.0,
        "escalate": False
    }

    # Step 1: Process
    state.update(process_node(state, retriever))

    # Step 2: Conditional Routing
    if state["escalate"]:
        state.update(hitl_node(state))

    return state