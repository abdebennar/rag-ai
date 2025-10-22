from langchain_huggingface import HuggingFaceEmbeddings
from config import *
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(f"Embedding using {device}")

embeddings = HuggingFaceEmbeddings(
    model_name=ModelName,
    model_kwargs={'device': device},
    encode_kwargs={
        'batch_size': 32 if device == 'cuda' else 128
    }
)