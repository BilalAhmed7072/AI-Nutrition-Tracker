# 🧠 AI Nutrition Tracker

An **AI-powered nutrition and diet assistant** that uses **Computer Vision**, **Retrieval-Augmented Generation (RAG)**, and **Google Gemini** to recognize food, analyze nutrition, and generate personalized meal plans.

---

## 🚀 Features

✅ **Food Recognition**  
Upload an image of food, and the system identifies it using a **Vision Transformer (ViT)** model from Hugging Face.

✅ **Automatic Nutrition Analysis**  
Fetches real-time nutrition data (calories, macros, total weight) using **Edamam/Nutritionix APIs**.

✅ **Personalized Diet Plan Generation**  
Generates daily meal plans using **Google Gemini 1.5 Flash**, based on:
- Gender, Age, Weight, Height  
- Activity Level  
- Health Goal (Weight Loss, Gain, Maintenance)

✅ **RAG-based Health Assistant**  
Retrieves verified health and nutrition information from your **vector store (FAISS)** using **LangChain + Google Generative AI Embeddings** for context-aware responses.

✅ **Flask Backend API**  
RESTful API endpoints for uploading images, generating diets, and querying health data.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask (Python) |
| **LLM** | Google Gemini 1.5 (via `google-generativeai`) |
| **Embedding & Vector DB** | LangChain, FAISS, HuggingFace Embeddings |
| **Vision Model** | `nateraw/food` (ViT Image Classifier) |
| **APIs** | Edamam & Nutritionix |
| **Database** | SQLite (SQLAlchemy ORM) |
| **Environment Config** | dotenv |

---

## 📁 Project Structure

