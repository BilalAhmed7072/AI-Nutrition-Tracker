import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

VECTOR_DIR = "data/vector_index"

def get_rag_response(query: str, k: int = 3) -> str:
    embeddings = GoogleGenerativeAIEmbeddings()
    db = FAISS.load_local(VECTOR_DIR, embeddings)
    docs = db.similarity_search(query, k=k)
    context = "\n\n".join([f"[{d.metadata.get('source','doc')}]\n{d.page_content}" for d in docs])

    prompt = f"""
You are a helpful, evidence-based health assistant. Use the context below when useful.

Context:
{context}

Question: {query}

Answer concisely and include actionable suggestions. If the context does not contain enough info, rely on best-practice nutrition guidance.
"""

    model = genai.GenerativeModel("gemini-1.5-pro")
    resp = model.generate_content(prompt)
    return resp.text
print("✅ RAG pipeline executed successfully!")

