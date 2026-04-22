import os
from dotenv import load_dotenv

load_dotenv()  # load .env file

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K = 5

PERSIST_DIR = "chroma_db"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

CONFIDENCE_THRESHOLD = 0.6

# Load API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")