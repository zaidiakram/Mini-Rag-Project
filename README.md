# 🔎 Mini RAG Application (Track B - AI Engineer Assessment)

## 📌 Project Overview
This project is a **Mini Retrieval-Augmented Generation (RAG) application** that enables users to ask questions over uploaded documents.  
The system processes PDFs into chunks, generates embeddings, stores them in a **cloud-hosted vector database (Pinecone)**, retrieves the most relevant chunks, applies a **reranker** for improved relevance, and finally uses an **LLM (Gemini)** to generate grounded answers with **citations**.  

The application is built with **Streamlit** for the frontend and can be deployed on a free hosting platform (e.g., Streamlit Cloud, Render, Railway).  
API keys are kept secure via `config.py` (local) or environment variables (deployment).  

---

## 🚀 Features
- 📂 Upload PDF and build a **knowledge base** in Pinecone.  
- 🔍 Retrieve top-k chunks with a **Retriever**.  
- 📊 Re-rank retrieved chunks with **Cohere Rerank**.  
- 🧠 Generate grounded answers with **Gemini LLM**, including inline **citations**.  
- 💻 Streamlit UI: file uploader, query box, answer display, citations.  
- 🔐 Secure API keys (`config.py` locally, environment vars in deployment).  

---

## 🏗️ Architecture







