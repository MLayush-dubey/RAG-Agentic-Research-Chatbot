# 🤖 RAG-Agentic Research Chatbot

A production-grade intelligent research assistant that combines Retrieval-Augmented Generation (RAG) with agent orchestration to provide deep insights from curated machine learning research papers.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.14.0-purple.svg)](https://www.llamaindex.ai/)

## 🌟 Key Features

- **Hybrid RAG Architecture**: Advanced document retrieval using LlamaIndex with ChromaDB vector store
- **Agent System**: CrewAI-powered agent orchestration for intelligent query processing
- **Production-Ready**: Dockerized deployment with FastAPI backend and Streamlit frontend
- **Research-Focused**: Pre-configured with 5 landmark ML research papers
- **Scalable Design**: Modular architecture supporting easy extension and customization

## 🏗️ Architecture Overview

```
RAG-Agentic-Research-Chatbot/
├── src/
│   ├── backend_src/          # FastAPI REST API
│   ├── frontend_src/          # Streamlit UI
│   ├── agents_src/            # CrewAI multi-agent system
│   └── rag_doc_ingestion/     # Document processing pipeline
├── documents/                 # Research papers corpus
├── vector_store/             # ChromaDB vector embeddings
├── Dockerfile                # Production container config
└── start.sh                  # Orchestration script
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM Provider** | Groq (Llama 3.1) | Fast inference with llama-3.1-8b-instant |
| **RAG Framework** | LlamaIndex | Document indexing & retrieval |
| **Vector Store** | ChromaDB | Persistent embedding storage |
| **Embeddings** | HuggingFace | Sentence transformers for semantic search |
| **Agent Framework** | CrewAI | Multi-agent orchestration & task delegation |
| **Backend API** | FastAPI | Async REST endpoints |
| **Frontend** | Streamlit | Interactive chat interface |
| **Containerization** | Docker | Reproducible deployment |

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Docker Desktop (for containerized deployment)
- Groq API Key ([Get one here](https://console.groq.com/))

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/MLayush-dubey/RAG-Agentic-Research-Chatbot.git
cd RAG-Agentic-Research-Chatbot
```

2. **Build the Docker image**
```bash
docker build -t rag-research-bot:latest .
```

3. **Run the container**
```bash
docker run -p 8000:8000 -p 8501:8501 \
  -e GROQ_API_KEY=your_groq_api_key \
  --name rag-research-bot-container-1 \
  rag-research-bot:latest
```

4. **Access the application**
   - Frontend UI: `http://localhost:8501`
   - Backend API: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

### Option 2: Local Development Setup

1. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp env_template.txt .env
```

Edit `.env` with your configuration:
```env
GROQ_API_KEY="your_groq_api_key"
DOCUMENTS_DIR="./documents"
VECTOR_STORE_DIR="./vector_store"
COLLECTION_NAME="document_collection"
MODEL_NAME="llama-3.1-8b-instant"
MODEL_TEMPERATURE=0.0
CHAT_ENDPOINT_URL="http://localhost:8000/chat/answer"
```

4. **Ingest documents** (one-time setup)
```bash
python -m src.rag_doc_ingestion.ingest_docs
```

5. **Start the services**
```bash
# Terminal 1: Backend
uvicorn src.backend_src.main:app --host 0.0.0.0 --port 8000

# Terminal 2: Frontend
streamlit run src/frontend_src/app.py --server.port 8501
```

## 🧠 System Components

### 1. RAG Document Ingestion Pipeline

- **Chunking Strategy**: Intelligent document splitting with context preservation
- **Embedding Model**: HuggingFace sentence-transformers for semantic embeddings
- **Vector Store**: ChromaDB with persistent storage for fast retrieval
- **Supported Formats**: PDF research papers with metadata extraction

### 2. Agent System (CrewAI)

The system employs specialized agents for different tasks:
- **Question-Answer Agent**: Retrieves the tool and provides accurate answers based on documents provided
- **Quality Assurance**: Validates responses for accuracy and relevance

### 3. Backend API (FastAPI)

**Key Endpoints:**
```
POST /chat/answer - Main chat interface
GET /docs - Interactive API documentation
```

**Features:**
- Async request handling for concurrent queries
- Pydantic validation for type safety
- Structured logging for production monitoring

### 4. Frontend Interface (Streamlit)

- Real-time streaming responses
- Chat history management
- Context-aware conversations
- Clean, intuitive UI design

## 📊 Performance Optimizations

1. **Vector Search**: ChromaDB indexing for sub-second retrieval
2. **Caching**: Embedded model caching to reduce latency
3. **Async Processing**: FastAPI async handlers for parallel request processing
4. **Groq Integration**: Fast inference with optimized Llama 3.1 model
5. **Docker Optimization**: Multi-stage builds with layer caching

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq API authentication key | Required |
| `DOCUMENTS_DIR` | Path to research papers | `./documents` |
| `VECTOR_STORE_DIR` | ChromaDB storage location | `./vector_store` |
| `COLLECTION_NAME` | Vector collection identifier | `document_collection` |
| `MODEL_NAME` | Groq model selection | `llama-3.1-8b-instant` |
| `MODEL_TEMPERATURE` | Response randomness (0-1) | `0.0` |
| `CHAT_ENDPOINT_URL` | Backend API endpoint | `http://localhost:8000/chat/answer` |

### Customizing the Knowledge Base

1. Add PDF research papers to the `documents/` directory
2. Re-run document ingestion:
```bash
python -m src.rag_doc_ingestion.ingest_docs
```
3. Restart the services to use the updated knowledge base

## 🧪 Testing Agent System

```bash
python -m src.agents_src.check_crew
```

This validates the CrewAI agent configuration and task execution flow.

## 📦 Project Structure

```
.
├── src/
│   ├── backend_src/
│   │   ├── main.py              # FastAPI application entry
│   │   └── models.py            # Pydantic schemas
│   ├── frontend_src/
│   │   └── app.py               # Streamlit interface
│   ├── agents_src/
│   │   ├── check_crew.py        # Agent testing
│   │   └── crew_config.yaml     # Agent definitions
│   └── rag_doc_ingestion/
│       └── ingest_docs.py       # Document processing
├── documents/                    # Research papers corpus
├── vector_store/                # ChromaDB persistence
├── .dockerignore                # Docker build exclusions
├── .env                         # Environment configuration
├── .gitignore                   # Git tracking exclusions
├── Dockerfile                   # Container definition
├── requirements.txt             # Python dependencies
├── start.sh                     # Service orchestration
└── README.md                    # This file
```

## 🔒 Security Considerations

- API keys stored in environment variables (never committed)
- `.env` file excluded via `.gitignore`
- Input validation through Pydantic models
- CORS configuration for production deployments

## 🐛 Troubleshooting

### Common Issues

**Problem**: Vector store not found
```bash
# Solution: Run document ingestion
python -m src.rag_doc_ingestion.ingest_docs
```

**Problem**: Port already in use
```bash
# Solution: Change ports in docker run command
docker run -p 8001:8000 -p 8502:8501 ...
```

**Problem**: Groq API rate limits
```bash
# Solution: Adjust MODEL_TEMPERATURE or implement retry logic
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **LlamaIndex** - RAG framework excellence
- **CrewAI** - Multi-agent orchestration
- **Groq** - Lightning-fast LLM inference
- **ChromaDB** - Efficient vector storage
- Research papers authors for advancing ML knowledge

## 📧 Contact

For questions, issues, or collaboration opportunities, please open an issue on GitHub.

---

⭐ If you find this project useful, please consider giving it a star on GitHub!

**Built with ❤️ for the ML Research Community**
