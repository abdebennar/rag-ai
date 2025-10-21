

from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import *

Splitter = RecursiveCharacterTextSplitter(chunk_size=TextSplitterChunkSize
							,chunk_overlap=TextSplitterChunkOverlap
							,length_function=TextSplitterLengthFucntion
							,add_start_index=TextSplitterAddStartIndex
)



