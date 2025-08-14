#!/bin/bash
# Startup script for the Calculator API

echo "🚀 Starting Calculator API..."
echo "================================"

# Detect environment and start PostgreSQL accordingly
if [ -n "$CODESPACES" ] || [ -n "$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN" ]; then
    # GitHub Codespace environment
    echo "📦 Starting PostgreSQL (GitHub Codespace)..."
    sudo service postgresql start 2>/dev/null || echo "PostgreSQL service not available"
    sleep 3
    sudo -u postgres createdb calculator_db 2>/dev/null || echo "Database already exists"
elif command -v systemctl >/dev/null 2>&1; then
    # Linux with systemd
    echo "📦 Starting PostgreSQL (Linux/systemd)..."
    sudo systemctl start postgresql 2>/dev/null || echo "PostgreSQL service not available"
    sleep 3
    sudo -u postgres createdb calculator_db 2>/dev/null || echo "Database already exists"
elif command -v brew >/dev/null 2>&1 && brew services list | grep -q postgresql; then
    # macOS with Homebrew PostgreSQL
    echo "📦 Starting PostgreSQL (macOS/Homebrew)..."
    brew services start postgresql@14 2>/dev/null || brew services start postgresql 2>/dev/null || true
    sleep 3
    createdb calculator_db 2>/dev/null || echo "Database already exists"
else
    echo "⚠️  PostgreSQL not found or not configured. API will work without database."
    echo "   To enable database features, install and configure PostgreSQL."
fi

# Install dependencies
echo "📥 Installing dependencies..."
if command -v uv >/dev/null 2>&1; then
    # Use uv if available
    uv sync
    echo "   Installing postgres extras..."
    uv pip install -e ".[postgres]"
else
    # Fallback to pip
    pip install -e ".[postgres]"
fi

# Determine Python command
PYTHON_CMD="python3"
if command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
fi

# Run database migrations (create tables) - only if PostgreSQL is available
echo "🔧 Setting up database tables..."
if command -v uv >/dev/null 2>&1; then
    uv run python -c "try:
        from codespace_learning.database.connection import engine, Base
        Base.metadata.create_all(bind=engine)
        print('✅ Database tables created')
    except Exception as e:
        print(f'⚠️  Database setup skipped: {e}')
        print('   API will work without database features')
    " 2>/dev/null || echo "⚠️  Database setup skipped - API will work without database features"
else
    python -c "try:
        from codespace_learning.database.connection import engine, Base
        Base.metadata.create_all(bind=engine)
        print('✅ Database tables created')
    except Exception as e:
        print(f'⚠️  Database setup skipped: {e}')
        print('   API will work without database features')
    " 2>/dev/null || echo "⚠️  Database setup skipped - API will work without database features"
fi

# Start the API server
echo "🌟 Starting FastAPI server on http://localhost:8000"
echo "📖 API Documentation: http://localhost:8000/docs"
echo "================================"

# Start the API server with proper environment
if command -v uv >/dev/null 2>&1; then
    uv run uvicorn codespace_learning.app:app --host 0.0.0.0 --port 8000 --reload
else
    uvicorn codespace_learning.app:app --host 0.0.0.0 --port 8000 --reload
fi