#!/bin/bash
# Simple API startup script for local development (no database required)

echo "🚀 Starting Simple Calculator API (No Database)..."
echo "================================"

echo "📥 Installing dependencies..."
uv sync

echo "🌟 Starting FastAPI server on http://localhost:8000"
echo "📖 API Documentation: http://localhost:8000/docs"
echo "================================"

uv run uvicorn codespace_learning.app_simple:app --host 0.0.0.0 --port 8000 --reload