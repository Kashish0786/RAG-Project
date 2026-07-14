from langchain_community.document_loaders import TextLoader

data = TextLoader("docloader/notes.txt")
doc = data.load()
print(doc)

