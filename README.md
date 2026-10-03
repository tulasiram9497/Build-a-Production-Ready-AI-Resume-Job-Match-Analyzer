# Build-a-Production-Ready-AI-Resume-Job-Match-Analyzer

A production-ready portfolio application for comparing a resume against one or more job descriptions using NLP, embeddings, semantic similarity, and explainable scoring.

## Overview

This project combines a React frontend with a Python FastAPI backend to analyze resume and job-description compatibility. The core pipeline performs PDF text extraction, skill normalization, sentence embedding similarity, structured skill matching, and explainable score generation. Results are stored in MongoDB when available and otherwise fall back to in-memory storage so the application still works locally without external services.

## Features

- PDF resume upload and text extraction
- Job description parsing and skill extraction
- Semantic similarity using sentence embeddings
- Explainable compatibility scoring from 0–100
- Matched vs missing skills
- Personalized learning roadmap
- Multi-job comparison
- Analysis history and detail views
- Strong validation, error handling, and API endpoints
- Docker and CI-ready project setup

## Stack

- Frontend: React, TypeScript, Vite, Tailwind
- Backend: Python, FastAPI, Pydantic
- ML: NumPy, Pandas, scikit-learn, sentence-transformers, PyMuPDF
- Data: MongoDB, JSON skill catalog
- DevOps: Docker, Docker Compose, GitHub Actions

## Running locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose up --build
```

## Environment variables

Create a `.env` file in the repository root using the example file:

```bash
cp .env.example .env
```

## API documentation

FastAPI auto-generates OpenAPI docs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

```bash
cd backend
pytest
```

```bash
cd frontend
npm test
```

## License

MIT
