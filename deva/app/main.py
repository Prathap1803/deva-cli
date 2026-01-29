import os

import time
from deva.config import DATA_DIR, CHROMA_DIR
from deva.ingestion.loaders import load_documents
from deva.ingestion.splitter import split_documents
from deva.ingestion.indexer import get_or_create_vectorstore
from deva.app.rag_chain import create_rag_chain

def main():
    # Check if vectorstore exists
    if not os.path.exists(CHROMA_DIR):
        print("🔹 Creating vector store from PDF...")
        # Your ingest logic here
        ...
    else:
        print("🔹 Loading existing vector store...")
        # Unified function replaces load_vectorstore
        vectorstore = get_or_create_vectorstore(reset=False)

    chain = create_rag_chain(vectorstore)

    # Interactive loop
    while True:
        query = input("Enter exit/quit to exit:\nPlease enter your query: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting Bye....")
            break
        response = chain.invoke(query)
        print(f"Answer: {response}\n")
