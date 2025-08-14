# GitHub Codespaces Learning Project

A Calculator API with PostgreSQL database designed to learn GitHub Codespaces and DevContainers.

## 🎯 Learning Objectives

- Understand GitHub Codespaces configuration with PostgreSQL
- Learn DevContainer setup and database integration
- Practice with FastAPI development in containers
- Explore automated development environment setup with databases
- Learn API development and testing

## 🚀 Quick Start with Codespaces

1. **Launch Codespace**: Click the green "Code" button and select "Create codespace on main"
2. **Or use direct link**: `https://codespaces.new/deepaks7n/codespace-learning?quickstart=1`

## 📁 Project Structure

```
├── .devcontainer/
│   └── devcontainer.json     # Codespace configuration with PostgreSQL
├── src/
│   ├── api/
│   │   └── calculator_endpoints.py  # FastAPI endpoints
│   ├── database/
│   │   └── connection.py     # Database connection and session
│   ├── models/
│   │   ├── calculation.py    # SQLAlchemy models
│   │   └── schemas.py        # Pydantic schemas
│   ├── calculator.py         # Calculator functions
│   ├── main.py              # CLI application
│   └── app.py               # FastAPI application
├── scripts/
│   └── start_api.sh         # API startup script
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Unit tests
├── requirements.txt          # Dependencies including FastAPI and PostgreSQL
├── pyproject.toml           # Project configuration
└── README.md
```

## 🚀 Running the Application

### Option 1: FastAPI Server (Recommended)
```bash
# Easy startup (handles PostgreSQL setup automatically)
./scripts/start_api.sh

# Manual startup
sudo service postgresql start
sudo -u postgres createdb calculator_db
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

**Access Points:**
- **API Documentation**: http://localhost:8000/docs (Interactive Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc
- **API Root**: http://localhost:8000

### Option 2: CLI Calculator
```bash
# Run the calculator demo
python src/main.py

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

## 🔧 DevContainer Features

This project demonstrates several DevContainer concepts:

### Base Image
- **Python 3.13** on Debian Bullseye
- Pre-configured Python development environment

### Features Added
- **Node.js LTS** - For frontend tooling if needed
- **GitHub CLI** - Direct GitHub integration
- **Docker-in-Docker** - Container support within container
- **PostgreSQL** - Full database server with automatic setup

### VS Code Extensions
- Python language support with Pylance
- GitHub Copilot for AI assistance  
- Black formatter and isort for code formatting
- Python environment management

### Post-Create Commands
- Installs `uv` for fast Python package management
- Sets up `llm` tool with GitHub Models integration
- Configures GPT-4o as default model for free AI assistance
- Starts PostgreSQL service automatically
- Creates calculator_db database

## 🌐 API Usage Examples

### Using curl
```bash
# Add two numbers
curl -X POST "http://localhost:8000/calculator/add" \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "operand1": 10, "operand2": 5}'

# Calculate square root
curl -X POST "http://localhost:8000/calculator/sqrt" \
  -H "Content-Type: application/json" \
  -d '{"operation": "sqrt", "operand": 16}'

# Calculate average
curl -X POST "http://localhost:8000/calculator/average" \
  -H "Content-Type: application/json" \
  -d '{"operation": "average", "numbers": [1, 2, 3, 4, 5]}'

# Get calculation history
curl "http://localhost:8000/calculator/history"
```

### Using Python requests
```python
import requests

# Add two numbers
response = requests.post(
    "http://localhost:8000/calculator/add",
    json={"operation": "add", "operand1": 10, "operand2": 5}
)
print(response.json())

# Get history
history = requests.get("http://localhost:8000/calculator/history")
print(history.json())
```

### Available Endpoints

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/calculator/add` | POST | Add two numbers | `{"operation": "add", "operand1": 10, "operand2": 5}` |
| `/calculator/subtract` | POST | Subtract numbers | `{"operation": "subtract", "operand1": 10, "operand2": 3}` |
| `/calculator/multiply` | POST | Multiply numbers | `{"operation": "multiply", "operand1": 4, "operand2": 5}` |
| `/calculator/divide` | POST | Divide numbers | `{"operation": "divide", "operand1": 20, "operand2": 4}` |
| `/calculator/power` | POST | Power operation | `{"operation": "power", "operand1": 2, "operand2": 3}` |
| `/calculator/modulo` | POST | Modulo operation | `{"operation": "modulo", "operand1": 10, "operand2": 3}` |
| `/calculator/sqrt` | POST | Square root | `{"operation": "sqrt", "operand": 16}` |
| `/calculator/factorial` | POST | Factorial | `{"operation": "factorial", "operand": 5}` |
| `/calculator/percentage` | POST | Percentage | `{"operation": "percentage", "part": 25, "whole": 200}` |
| `/calculator/average` | POST | Average | `{"operation": "average", "numbers": [1,2,3,4,5]}` |
| `/calculator/median` | POST | Median | `{"operation": "median", "numbers": [1,3,5,7,9]}` |
| `/calculator/history` | GET | Get calculation history | - |
| `/calculator/history/{id}` | GET | Get specific calculation | - |

## 🗄️ Database Integration

- **PostgreSQL** automatically configured and started
- **Calculation history** stored permanently  
- **SQLAlchemy ORM** for database operations
- **Automatic table creation** on startup
- **Environment variables** for easy configuration

## 🎓 Learning Concepts

### 1. **DevContainer Configuration**
The `.devcontainer/devcontainer.json` file defines:
- Base Docker image to use
- Additional features to install
- VS Code settings and extensions
- Environment variables and port forwarding

### 2. **Codespace Benefits**
- ✅ Consistent development environment
- ✅ No local setup required  
- ✅ Works entirely in browser
- ✅ Perfect for workshops and collaboration
- ✅ Quick recovery if environment breaks

### 3. **Workshop Ready**
- Skip the 30-minute setup phase
- Everyone gets identical environment
- Focus on learning, not troubleshooting
- Easy to reset and start fresh

## 🔗 Useful Links

- **Direct Codespace**: `https://codespaces.new/deepaks7n/codespace-learning?quickstart=1`
- **GitHub Codespaces Docs**: https://docs.github.com/en/codespaces
- **DevContainer Spec**: https://containers.dev/
- **Available Images**: https://github.com/devcontainers/images
- **Available Features**: https://github.com/devcontainers/features