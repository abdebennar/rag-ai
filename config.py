from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


DataPath  = "/goinfre/abennar/rag-ai/content/files/en-us"
FilesTypeGlob = "**/*.md"
ChromaPath = "embeddings"


# Loader Settings

LoaderMultitthreading= True
LoaderConcurrency=10
LoaderShowProgress=True


def token_length(text):
    """Count tokens instead of characters"""
    return len(tokenizer.encode(text))

ModelName="sentence-transformers/all-MiniLM-L6-v2"
TextSplitterChunkSize=256
TextSplitterChunkOverlap=25
TextSplitterLengthFucntion=token_length
TextSplitterAddStartIndex=True

