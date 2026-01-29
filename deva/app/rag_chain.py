from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from deva.config import llm
from deva.app.prompts import RAG_PROMPT
from deva.app.retriever import get_retriever, format_docs

def create_rag_chain(vectorstore):
    retriever = get_retriever(vectorstore)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain
