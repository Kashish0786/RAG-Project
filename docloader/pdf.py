# from langchain_community.document_loaders import PyPDFLoader

# data = PyPDFLoader("docloader/GRU.pdf")
# doc = data.load()
# # print(len(doc))  # 15 page of pdf 
# print(doc[14]) # 14 page data

# token chunk splitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("docloader/GRU.pdf")

doc = data.load()

splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap=10
)

chunks = splitter.split_documents(doc)

# without page content metadata will also be seen
print(chunks[0].page_content)
# also see RecursiveCharacterTextSplitter , just replace texttokensplitter by it