from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from scripts.prompt import rag_chat_prompt

def format_docs(docs):
    """Format retrieved documents into a single string"""
    return "\n\n".join(doc.page_content for doc in docs)

def create_rag_chain(retriever, llm):
    """Create a complete RAG chain"""
    
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | rag_chat_prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain