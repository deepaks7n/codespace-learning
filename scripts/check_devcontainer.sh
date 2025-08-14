#!/bin/bash
# Check DevContainer and Docker Compose status

echo "🔍 DevContainer Status Check"
echo "================================"

# Check if we're in a DevContainer
if [ -n "$CODESPACES" ] || [ -n "$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN" ]; then
    echo "✅ Running in GitHub Codespace"
elif [ -f "/.dockerenv" ]; then
    echo "✅ Running in Docker container (DevContainer)"
else
    echo "❌ Not running in a container environment"
fi

# Check database connectivity
echo ""
echo "🔗 Database Connection Test:"
if command -v psql >/dev/null 2>&1; then
    echo "✅ PostgreSQL client available"
    
    if psql postgresql://postgres:postgres@db/calculator_db -c "SELECT version();" 2>/dev/null; then
        echo "✅ Database connection successful"
    else
        echo "❌ Database connection failed"
        echo "   Tip: Database service might still be starting up"
    fi
else
    echo "❌ PostgreSQL client not found"
fi

# Check if database service is reachable
echo ""
echo "🌐 Network Test:"
if command -v nc >/dev/null 2>&1; then
    if nc -z db 5432 2>/dev/null; then
        echo "✅ PostgreSQL service reachable at db:5432"
    else
        echo "❌ PostgreSQL service not reachable"
    fi
else
    echo "⚠️  netcat not available for network test"
fi

# Check Python environment
echo ""
echo "🐍 Python Environment:"
if command -v uv >/dev/null 2>&1; then
    echo "✅ uv package manager available"
    if [ -d ".venv" ]; then
        echo "✅ Virtual environment exists"
    else
        echo "⚠️  Virtual environment not found"
    fi
else
    echo "❌ uv not found"
fi

# Check environment variables
echo ""
echo "📝 Environment Variables:"
if [ -n "$DATABASE_URL" ]; then
    echo "✅ DATABASE_URL: $DATABASE_URL"
else
    echo "❌ DATABASE_URL not set"
fi

if [ -n "$PYTHONPATH" ]; then
    echo "✅ PYTHONPATH: $PYTHONPATH"
else
    echo "⚠️  PYTHONPATH not set"
fi

echo ""
echo "📋 Quick Actions:"
echo "  Test API: curl http://localhost:8000/health"
echo "  Start API: ./scripts/start_api.sh"
echo "  Simple API: ./scripts/start_simple_api.sh"