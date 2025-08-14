#!/bin/bash
# Startup script for the Calculator API

echo "🚀 Starting Calculator API..."
echo "================================"

# Start PostgreSQL if not running
echo "📦 Starting PostgreSQL..."
sudo service postgresql start

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 3

# Create database if it doesn't exist
echo "🗄️  Setting up database..."
sudo -u postgres createdb calculator_db 2>/dev/null || echo "Database already exists"

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "📥 Installing dependencies..."
    uv venv
    uv pip install -r requirements.txt
fi

# Run database migrations (create tables)
echo "🔧 Creating database tables..."
python -c "from src.database.connection import engine, Base; Base.metadata.create_all(bind=engine); print('✅ Database tables created')"

# Start the API server
echo "🌟 Starting FastAPI server on http://localhost:8000"
echo "📖 API Documentation: http://localhost:8000/docs"
echo "================================"

uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload