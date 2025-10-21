from langchain_huggingface import HuggingFaceEmbeddings
from config import *

embeddings = HuggingFaceEmbeddings(
    model_name=ModelName
)