from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredFileLoader, UnstructuredHTMLLoader
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
import os

# Set API key
os.environ['OPENAI_API_KEY'] = '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'

# Load Data
loader = UnstructuredHTMLLoader("dhaka_stock_exchange.html")
raw_documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(raw_documents)


# Load Data to vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)


# Save vectorstore
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)
