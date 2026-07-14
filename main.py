# text summarization
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_community.document_loaders import TextLoader
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# data = TextLoader("docloader/notes.txt")
# docs = data.load()

# template = ChatPromptTemplate.from_messages(
#     [("system, you are ai that ummarize the text"),
#     ("human" ,"{data}")]
# )
# model = ChatMistralAI(model = "mistral-small-2506")
# prompt = template.format_messages(data=docs[0].page_content)

# result = model.invoke(prompt)

# print(result.content)

# pdf loader
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = PyPDFLoader("docloader/GRU.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [("system, you are ai that ummarize the text"),
    ("human" ,"{data}")]
)
model = ChatMistralAI(model = "mistral-small-2506")
prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)

print(result.content)

#  currently the pdf contain 15 page so it easy to get output but when pdf have 100,300 pages we have to use chunks