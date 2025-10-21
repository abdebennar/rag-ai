
from langchain_community.vectorstores import Chroma
from config import *



def CreateChromaVecDB(chunks, embedding):
	vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=ChromaPath)
	return vectordb



