from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config import settings
from backend.app.api.routes.analysis import router as analysis_router
from backend.app.api.routes.jobs import router as jobs_router
from backend.app.api.routes.resume import router as resume_router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="AI Resume & Job Match Analyzer API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router, prefix="/api")
app.include_router(jobs_router, prefix="/api")
app.include_router(analysis_router, prefix="/api")


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"status": "ok", "service": settings.app_name}
