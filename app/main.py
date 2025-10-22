from scripts.loader import DocsLoader
from scripts.splitter import Splitter
from scripts.chroma import CreateChromaVecDB
from scripts.embeddings import embeddings
from scripts.chain import create_rag_chain
from langchain_groq import ChatGroq
from langchain_chroma import Chroma 
from dotenv import load_dotenv
from config import *
import os

load_dotenv()

if os.path.exists(ChromaPath) and os.listdir(ChromaPath):
    print("✓ Loading existing vector database...")
    chromadb = Chroma(
        persist_directory=ChromaPath,
        embedding_function=embeddings
    )
    try:
        count = chromadb._collection.count()
        print(f"✓ Loaded existing database with {count} chunks.")
    except:
        print(f"✓ Loaded existing database from {ChromaPath}")
else:
    print("Loading documents...")
    docs = DocsLoader(DataPath, FilesTypeGlob)
    chunks = Splitter.split_documents(docs)
    print(f"✓ Split {len(docs)} documents into {len(chunks)} chunks.")
    
    print("Creating vector database...")
    chromadb = CreateChromaVecDB(chunks, embeddings)
    print(f"✓ Saved {len(chunks)} chunks to {ChromaPath}")

retriever = chromadb.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)

print("Loading LLM...")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

rag_chain = create_rag_chain(retriever, llm)

print("\n" + "="*50)
print("RAG System Ready! Ask questions about your documents.")
print("Type 'quit' to exit.")
print("="*50 + "\n")

while True:
    question = input("Question: ")
    
    if question.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    
    if not question.strip():
        continue
    
    print("\nThinking...\n")
    
    try:
        answer = rag_chain.invoke(question)
        print(f"Answer: {answer}\n")
        print("-" * 50 + "\n")
    except Exception as e:
        print(f"Error: {e}\n")