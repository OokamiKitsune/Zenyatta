# 📦 Retrieval-Augmented Question Answering (RAG) Assistant

This project is a modular retrieval-augmented generation (RAG) system that uses local documents and Large Language Models (LLMs) to answer questions with accurate, context-aware responses.

It is designed to:
- Load and process `.pdf` and `.txt` files from a directory
- Embed document chunks into a vector store
- Retrieve relevant context based on user queries
- Generate answers with an LLM
- Serve responses through a web interface

You can adapt this system for any domain: internal knowledge bases, SOP documentation, product manuals, or training materials.

---

## ✨ Features

✅ Load and parse local files (`.pdf` and `.txt`)  
✅ Embed documents using modern embeddings (e.g., Ollama)  
✅ Store embeddings persistently in ChromaDB  
✅ Incrementally update your knowledge base  
✅ Query documents through a clean front end (Gradio)  
✅ Customize LLM prompts to set scope, tone, and disclaimers

---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```