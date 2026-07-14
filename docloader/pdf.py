from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("docloader/GRU.pdf")
doc = data.load()
# print(len(doc))  # 15 page of pdf 
print(doc[14]) # 14 page data