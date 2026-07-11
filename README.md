# AI Study Assistant — RAG-Powered Study Companion

A Retrieval-Augmented Generation (RAG) application that lets users upload their own study material and ask natural-language questions about it, with answers grounded in the actual document content rather than general model knowledge.

## Problem

Students working through dense study material (textbooks, lecture notes, research papers) often need quick, accurate answers to specific questions — but general-purpose chatbots either hallucinate details or lack the context of the exact material being studied. This project solves that by grounding every answer in the user's own uploaded documents.

## How It Works

1. **Ingestion** — User uploads a PDF of study material.
2. **Chunking** — The document is split into semantically coherent chunks for retrieval.
3. **Embedding** — Chunks are embedded using TinyLlama embeddings and stored in a ChromaDB vector store.
4. **Retrieval** — When a user asks a question, the most relevant chunks are retrieved via semantic similarity search.
5. **Generation** — Retrieved context is passed to Google Gemini via LangChain to generate a grounded, context-aware answer.
6. **Interface** — All of this is exposed through an interactive Streamlit UI for natural-language querying.

## Tech Stack

- **LLM**: Google Gemini
- **Orchestration**: LangChain
- **Vector Store**: ChromaDB
- **Embeddings**: TinyLlama
- **Frontend**: Streamlit
- **Language**: Python

## Features

- PDF ingestion and automatic chunking
- Semantic (vector-based) retrieval over uploaded documents
- Context-grounded question answering — reduces hallucination compared to ungrounded LLM responses
- Simple, interactive chat-style interface for querying uploaded material

## Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API key

### Installation
```bash
git clone <your-repo-url>
cd ai-study-assistant
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

### Run Locally
```bash
streamlit run app.py
```

## Usage

1. Launch the app and upload a PDF from the sidebar.
2. Wait for the document to be chunked and indexed into the vector store.
3. Ask questions about the material in the chat interface.
4. Answers are generated using only the retrieved, relevant context from your document.

## Project Status

This is an actively developed project. Planned upgrades include:
- Multi-agent architecture (quiz/flashcard generation, summarization, roadmap generation, and web search agents) orchestrated via a routing layer
- An evaluation harness to measure retrieval accuracy and answer quality
- Hybrid search (keyword + semantic) and re-ranking for improved retrieval
- Migration from Streamlit-only frontend to a FastAPI-backed deployment
- Request/response tracing and observability

## License

MIT
