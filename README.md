# 🤖 RAG-Based Customer Support Assistant (LangGraph + HITL)

An intelligent **Retrieval-Augmented Generation (RAG)** system designed to automate customer support using a PDF knowledge base.
Built with **LangGraph**, **ChromaDB**, and **Groq LLM**, this system delivers accurate, context-aware responses and supports **Human-in-the-Loop (HITL)** escalation.

---

##  Features

*  **PDF Knowledge Base Processing**
*  **Chunking & Embedding (Sentence Transformers)**
*  **Semantic Search using ChromaDB**
*  **LLM Response Generation (Groq API)**
*  **Graph-based Workflow (LangGraph)**
*  **Conditional Routing (Answer vs Escalate)**
*  **Human-in-the-Loop (HITL) Support**
*  **Streamlit Chat UI**
*  **Confidence Scoring**

---

##  What is RAG?

**Retrieval-Augmented Generation (RAG)** combines:

*  Retrieval → Fetch relevant context from documents
*  Generation → Use LLM to generate grounded answers

 This reduces hallucination and improves accuracy.

---

##  System Architecture

```text
User (Streamlit UI)
        │
        ▼
   Query Input
        │
        ▼
 LangGraph Workflow
        │
 ┌───────────────┐
 │ Intent Router │
 └──────┬────────┘
        │
   ┌────┴─────┐
   ▼          ▼
  RAG       HITL
  Flow     Escalation
   │            │
   ▼            ▼
Retriever     Human Agent
   │            │
   ▼            ▼
LLM        Response Input
   │            │
   └──────┬─────┘
          ▼
      Final Output
```

## 2. Data Ingestion Architecture
PDF Document
     │
     ▼
Document Loader (PyPDF)
     │
     ▼
Text Chunking (800 tokens + overlap)
     │
     ▼
Embedding Model (Sentence Transformers)
     │
     ▼
Vector Storage (ChromaDB)


## 3. Query Processing Flow
User Query
   │
   ▼
Convert to Embedding
   │
   ▼
Retrieve Top-K Similar Chunks (ChromaDB)
   │
   ▼
Pass Context + Query to LLM (Groq)
   │
   ▼
Generate Answer
   │
   ▼
Confidence Check
   │
   ├── High Confidence → Return Answer
   │
   └── Low Confidence → HITL Escalation

---

##  Project Structure

```bash
rag_customer_support/
│
├── app.py
├── streamlit_app.py
├── config.py
│
├── ingestion/
│   ├── loader.py
│   ├── chunking.py
│   └── embed_store.py
│
├── retrieval/
│   └── retriever.py
│
├── llm/
│   └── generator.py
│
├── graph/
│   └── workflow.py
│
├── hitl/
│   └── human_loop.py
│
├── utils/
│   └── helpers.py
│
├── data/
│   └── knowledge_base.pdf
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/rag-customer-support.git
cd rag-customer-support
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file in root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

---

## ▶️ Run the Application

### 🔹 CLI Mode

```bash
python app.py
```

---

### 🔹 Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

##  How It Works

###  Ingestion Pipeline

```text
PDF → Load → Chunk → Embed → Store (ChromaDB)
```

###  Query Flow

```text
User Query
→ Retrieve Relevant Chunks
→ LLM Generates Answer
→ Confidence Check
→ HITL (if needed)
→ Response
```

---

##  LangGraph Workflow

* **Node 1:** Processing (Retrieval + LLM)
* **Node 2:** Output
* **Conditional Routing:** Based on confidence

---

##  Human-in-the-Loop (HITL)

Triggered when:

* Low confidence
* No relevant context
* Complex queries

👉 Human response overrides AI output.

---

##  Example Output

```text
Q: What are the rules for refund of fees?

A:
• Applicable to undergraduate and postgraduate programs  
• Full refund before deadline  
• Partial refund after admission confirmation  
• No refund after final cutoff  

Confidence: 0.91
```

---

##  Challenges & Trade-offs

| Challenge         | Solution                |
| ----------------- | ----------------------- |
| Hallucination     | RAG with context        |
| Latency           | Optimize Top-K          |
| Accuracy vs Speed | Balanced chunk size     |
| Model changes     | Dynamic config via .env |

---

##  Future Enhancements

*  Multi-document support
*  Conversational memory
*  Deployment (AWS / Docker)
*  Feedback learning loop
* 📌 Source citation highlighting

---

## 🧪 Tech Stack

* **Python**
* **LangChain + LangGraph**
* **ChromaDB**
* **Groq LLM**
* **Sentence Transformers**
* **Streamlit**

---

## 📌 Key Highlights

✔ Production-style architecture
✔ Graph-based control flow
✔ Real-time LLM integration
✔ Human fallback mechanism

---

## 🙌 Acknowledgment

This project demonstrates a real-world application of:

* RAG Systems
* Workflow Orchestration
* AI + Human Collaboration

