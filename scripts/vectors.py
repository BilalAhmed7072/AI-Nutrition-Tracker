import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_FOLDER = "../data"
PERSIST_DIR = "data/vector_index"

def build_vectorstore():
    docs = []
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(DATA_FOLDER, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    docs.append(Document(page_content=text, metadata={"source": filename}))

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(PERSIST_DIR)
    print("✅ Vector store built at", PERSIST_DIR)

if __name__ == "__main__":
    build_vectorstore()
