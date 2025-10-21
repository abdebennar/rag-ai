from langchain_community.document_loaders import DirectoryLoader, TextLoader


def DocsLoader(Path, FilesType):
	loader = DirectoryLoader(Path, glob=FilesType)
	documents = loader.load()
	return documents
