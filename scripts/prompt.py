from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

# RAG Prompt Template
RAG_TEMPLATE = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Keep the answer concise and relevant.

Context: {context}

Question: {question}

Answer:"""

rag_prompt = PromptTemplate(
    template=RAG_TEMPLATE,
    input_variables=["context", "question"]
)

RAG_CHAT_TEMPLATE = """You are a helpful assistant that answers questions based on the provided context.

Context:
{context}

Question: {question}

Please provide a clear and concise answer based only on the context above. If the context doesn't contain the answer, say "I don't have enough information to answer that question."
"""

rag_chat_prompt = ChatPromptTemplate.from_template(RAG_CHAT_TEMPLATE)