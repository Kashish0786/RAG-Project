from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/mackbook-pro/"

data = WebBaseLoader(url)

doc = data.load()

print(doc[0].page_content)
