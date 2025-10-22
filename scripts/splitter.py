from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
from config import *




print("Loading tokenizer for accurate chunk splitting...")
tokenizer = AutoTokenizer.from_pretrained(ModelName)



Splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=25,
    length_function=len,
    add_start_index=True,
    separators=["\n\n", "\n", ". ", " ", ""],
)

print(f"✓ Splitter configured: {256} tokens per chunk, {25} token overlap")



