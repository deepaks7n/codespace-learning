"""FastAPI application for Calculator API."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database.connection import engine, Base
from src.api.calculator_endpoints import router as calculator_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Create database tables
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Calculator API",
    description="A calculator API with PostgreSQL storage for learning GitHub Codespaces",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculator_router)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Calculator API",
        "description": "A learning project for GitHub Codespaces with PostgreSQL",
        "endpoints": {
            "calculator": "/calculator/*",
            "docs": "/docs",
            "openapi": "/openapi.json",
        },
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Calculator API is running"}