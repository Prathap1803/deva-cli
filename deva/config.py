
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings

DATA_DIR = "./data"
CHROMA_DIR = "./deva_cli/storage/chroma_db"

llm = OllamaLLM(
    model="dolphin-mistral",
    base_url="http://localhost:11434",
    temperature=0.3
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
