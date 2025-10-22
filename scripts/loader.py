from langchain_community.document_loaders import DirectoryLoader, TextLoader
from config import *


def DocsLoader(Path, FilesType):
	loader = DirectoryLoader(Path, glob=FilesType,
						  loader_cls=TextLoader
						  ,loader_kwargs={'autodetect_encoding': True}
						  ,use_multithreading=LoaderMultitthreading
						  ,max_concurrency=LoaderConcurrency
						  ,show_progress=LoaderShowProgress)
	documents = loader.load()
	return documents
