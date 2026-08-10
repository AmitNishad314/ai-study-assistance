# 📚 AI Study Assistance

> An end-to-end AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions grounded only in the uploaded content.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react"/>
  <img src="https://img.shields.io/badge/LangChain-RAG-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ChromaDB-VectorDB-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Gemini-LLM-orange?style=for-the-badge"/>
</p>

---

## 🚀 Live Demo

### Frontend
https://ai-study-assistance-gules.vercel.app/

### Backend API
https://ai-study-assistance-sbjs.onrender.com/

### API Documentation
https://ai-study-assistance-sbjs.onrender.com/docs

---

# 📖 Overview

AI Study Assistance is an AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**.

Instead of answering from the model's own knowledge, it retrieves the most relevant chunks from uploaded PDFs using semantic search and generates answers strictly from those retrieved documents.

This significantly reduces hallucinations while enabling users to interact with long PDF documents naturally.

---

# ✨ Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Gemini Embedding generation
- 🗂️ ChromaDB vector storage
- 🔍 Semantic similarity search
- 🤖 Gemini-powered answer generation
- 📑 Source citation with page numbers
- 🗑️ Delete uploaded documents
- 📋 List indexed documents
- 🌐 REST API with FastAPI
- ⚡ React frontend
- 🐳 Dockerized backend
- ☁️ Deployed on Render & Vercel

---

# 🏗️ System Architecture

```
                    +-------------------+
                    |   React Frontend  |
                    +---------+---------+
                              |
                              |
                     Axios REST API
                              |
                              ▼
                    +-------------------+
                    |     FastAPI       |
                    +---------+---------+
                              |
          +-------------------+------------------+
          |                                      |
          ▼                                      ▼
 PDF Upload Pipeline                     Chat Pipeline
          |                                      |
 PDF Loader                          User Question
          |                                      |
 Text Splitter                         Embed Query
          |                                      |
 Embedding Model                   Similarity Search
          |                                      |
 Chroma Vector DB  <-----------------------------+
          |
 Retrieved Chunks
          |
 Prompt Template
          |
 Gemini LLM
          |
 Final Response
```

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- Axios
- Tailwind CSS
- React Markdown
- Lucide React
- React Hot Toast

---

## Backend

- FastAPI
- LangChain
- ChromaDB
- Google Gemini
- Uvicorn
- Pydantic

---

## AI Stack

- Gemini Embeddings
- Gemini Flash LLM
- Retrieval-Augmented Generation (RAG)
- Semantic Search

---

## Deployment

- Docker
- Render
- Vercel

---

# 📂 Project Structure

```
AI-Document-Assistant-V2
│
├── app
│   ├── api
│   ├── core
│   ├── documents
│   ├── embeddings
│   ├── generation
│   ├── llm
│   ├── prompts
│   ├── retrieval
│   ├── schemas
│   ├── services
│   ├── utils
│   └── vector_store
│
├── frontend
│
├── storage
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone https://github.com/AmitNishad314/ai-study-assistance.git
cd ai-study-assistance
```

---

## Backend Setup

Create virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash

UPLOAD_DIR=storage/uploads
CHROMA_DIR=storage/chroma_db
```

---

Run backend

```bash
python main.py
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

Frontend Environment Variable

```
VITE_API_URL=http://127.0.0.1:8000
```

---

# 🐳 Docker

Build image

```bash
docker build -t ai-study-assistance .
```

Run container

```bash
docker run -p 8000:8000 ai-study-assistance
```

---

# 📡 API Endpoints

## Upload PDF

```
POST /upload
```

---

## Ask Question

```
POST /chat
```

---

## Get Documents

```
GET /documents
```

---

## Delete Document

```
DELETE /documents/{document_id}
```

---

# 🧠 RAG Workflow

```
User Uploads PDF
        │
        ▼
PDF Loader
        │
        ▼
Text Splitter
        │
        ▼
Gemini Embeddings
        │
        ▼
ChromaDB
        │
        ▼
User Question
        │
        ▼
Similarity Search
        │
        ▼
Relevant Chunks
        │
        ▼
Prompt Template
        │
        ▼
Gemini Flash
        │
        ▼
Answer + Sources
```

---

# 📸 Screenshots

## Home Page

_Add screenshot_

---

## Upload PDF

_Add screenshot_

---

## Chat Interface

_Add screenshot_

---

## Source Citation

_Add screenshot_

---

## Swagger API

_Add screenshot_

---

# 💡 Challenges Solved

- Built a complete Retrieval-Augmented Generation (RAG) pipeline from scratch.
- Implemented semantic document retrieval using vector embeddings.
- Integrated LangChain with Google's Gemini models.
- Managed persistent vector storage using ChromaDB.
- Designed a modular FastAPI backend.
- Connected React frontend with FastAPI backend.
- Containerized the backend using Docker.
- Deployed backend on Render and frontend on Vercel.
- Implemented source attribution for generated answers.
- Added document upload, indexing, retrieval, and deletion functionality.

---

# 🚧 Current Limitations

- Uses free Gemini API quota.
- No authentication.
- No conversation history.
- Supports only PDF files.
- Single-user document collection.
- No streaming responses.
- No background indexing queue.

---

# 🚀 Future Improvements

## High Priority

- [ ] Authentication (Google OAuth / JWT)
- [ ] User-specific document collections
- [ ] Multi-user support
- [ ] Streaming AI responses
- [ ] Better exception handling
- [ ] Friendly error messages
- [ ] Retry mechanism for Gemini API failures
- [ ] Environment-based CORS configuration

---

## AI Improvements

- [ ] Hybrid Search (Vector + BM25)
- [ ] Query rewriting
- [ ] Context compression
- [ ] Parent Document Retriever
- [ ] Multi-query retrieval
- [ ] Metadata-aware retrieval
- [ ] Better chunking strategy
- [ ] Reranking retrieved documents
- [ ] Support multiple LLM providers
- [ ] Conversation memory

---

## Document Features

- [ ] DOCX support
- [ ] TXT support
- [ ] Markdown support
- [ ] OCR for scanned PDFs
- [ ] Drag & Drop upload
- [ ] Batch uploads
- [ ] Folder upload
- [ ] Duplicate document detection

---

## UI Improvements

- [ ] Dark mode
- [ ] Mobile responsiveness
- [ ] Typing animation
- [ ] Markdown rendering improvements
- [ ] Better loading indicators
- [ ] Upload progress bar
- [ ] Chat history
- [ ] Copy answer button
- [ ] Download conversation
- [ ] Theme customization

---

## Backend Improvements

- [ ] Background workers (Celery/RQ)
- [ ] Redis caching
- [ ] Async document processing
- [ ] Logging dashboard
- [ ] Health checks
- [ ] Unit tests
- [ ] Integration tests
- [ ] CI/CD using GitHub Actions
- [ ] Docker Compose
- [ ] Kubernetes deployment

---

## DevOps

- [ ] Nginx reverse proxy
- [ ] HTTPS certificates
- [ ] Monitoring with Prometheus
- [ ] Grafana dashboard
- [ ] Rate limiting
- [ ] API analytics
- [ ] Secrets management
- [ ] Automatic deployment pipeline

---

# 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- LangChain
- Prompt Engineering
- Vector Databases
- Embedding Models
- FastAPI Backend Development
- React Frontend Development
- REST API Design
- Docker
- Render Deployment
- Vercel Deployment
- Environment Variable Management
- Production Debugging
- AI Application Deployment

---

# 👨‍💻 Author

**Amit Nishad**

GitHub: https://github.com/AmitNishad314

LinkedIn: _Add LinkedIn URL_

---

# ⭐ If you found this project useful, consider giving it a star!