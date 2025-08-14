"""FastAPI application for Calculator API."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import database components, but don't fail if they're not available
database_available = False
try:
    from .database.connection import engine, Base
    from .api.calculator_endpoints import router as calculator_router
    database_available = True
    logger.info("Database components loaded successfully")
except Exception as e:
    logger.warning(f"Database components not available: {e}")
    logger.info("Running in database-free mode")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    if database_available:
        try:
            # Create database tables
            Base.metadata.create_all(bind=engine)
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.warning(f"Failed to create database tables: {e}")
            logger.info("Continuing without database features")
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

# Include database router only if available
if database_available:
    app.include_router(calculator_router)
    logger.info("Database-enabled calculator endpoints loaded")
else:
    # Import and include simple endpoints instead
    from .api.simple_endpoints import router as simple_router
    app.include_router(simple_router)
    logger.info("Database-free calculator endpoints loaded")


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


def start_server():
    """Start the FastAPI server."""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)