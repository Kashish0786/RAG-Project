# from langchain_community.document_loaders import TextLoader

# data = TextLoader("docloader/notes.txt")
# doc = data.load()
# print(doc)

# character chunk
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import characterTextSplitter

splitter = characterTextSplitter(
    separator="", #seprate by this
    chunk_size = 10,
    chunk_overlap=1
)
data = TextLoader("docloader/notes.txt")
doc = data.load()
chunks = splitter.split_documents(doc)

for i in chunks:
    print(i.page_content)
    print()
    print()
