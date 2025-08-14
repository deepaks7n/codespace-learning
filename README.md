# GitHub Codespaces Learning Project

A Calculator API with PostgreSQL database designed to learn GitHub Codespaces and DevContainers.

## 🎯 Learning Objectives

- Understand GitHub Codespaces configuration with PostgreSQL
- Learn DevContainer setup and database integration
- Practice with FastAPI development in containers
- Explore automated development environment setup with databases
- Learn API development and testing

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended for Learning)

#### Step-by-Step Codespace Setup:
1. **Launch Codespace**: 
   - Go to [this repository](https://github.com/deepaks7n/codespace-learning)
   - Click the green "Code" button → "Codespaces" tab → "Create codespace on main"
   - **Or use direct link**: `https://codespaces.new/deepaks7n/codespace-learning?quickstart=1`

2. **Automatic Configuration** (takes 2-3 minutes):
   - Docker Compose builds the app and database containers
   - PostgreSQL 15 starts in background with persistent storage
   - Python 3.13 environment with all dependencies installed
   - Environment variables configured automatically

3. **Verify Setup**:
   ```bash
   # Check DevContainer status (comprehensive)
   ./scripts/check_devcontainer.sh
   
   # Or test database connection directly
   psql postgresql://postgres:postgres@db/calculator_db -c "SELECT version();"
   
   # Start the API server
   ./scripts/start_api.sh
   ```
   
   **Note**: In DevContainers, you're already inside the app container. The database runs as a separate service that's automatically managed.

4. **Access Your Application**:
   - **API Documentation**: Click "Open in Browser" when port 8000 is forwarded, then add `/docs`
   - **Or manually**: http://localhost:8000/docs
   - **Test endpoint**: http://localhost:8000/health

### Option 2: Local Development 
```bash
# Clone the repository
git clone https://github.com/deepaks7n/codespace-learning.git
cd codespace-learning

# Quick start (no database required)
./scripts/start_simple_api.sh

# Or full setup with PostgreSQL
./scripts/start_api.sh
```

## 📁 Project Structure

```
├── .devcontainer/
│   ├── devcontainer.json     # Codespace configuration
│   ├── docker-compose.yml    # Multi-container setup (app + PostgreSQL)
│   └── Dockerfile           # Custom Python environment
├── codespace_learning/
│   ├── api/
│   │   └── calculator_endpoints.py  # FastAPI endpoints
│   ├── database/
│   │   └── connection.py     # Database connection and session
│   ├── models/
│   │   ├── calculation.py    # SQLAlchemy models
│   │   └── schemas.py        # Pydantic schemas
│   ├── calculator.py         # Calculator functions
│   ├── main.py              # CLI application
│   ├── app.py               # FastAPI application (with database)
│   └── app_simple.py        # FastAPI application (no database)
├── scripts/
│   ├── start_api.sh         # Full API startup script (with PostgreSQL)
│   └── start_simple_api.sh  # Simple API startup script (no database)
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Unit tests
├── requirements.txt          # Dependencies including FastAPI and PostgreSQL
├── pyproject.toml           # Project configuration
└── README.md
```

## 🚀 Running the Application

### Local Development

#### Simple API (No Database) - **Best for Local Testing**
```bash
./scripts/start_simple_api.sh
```
- ✅ Works immediately on any system
- ✅ No PostgreSQL required
- ✅ All calculator functions available
- ❌ No calculation history storage

#### Full API (With PostgreSQL)
```bash
./scripts/start_api.sh
```
- ✅ Full database integration
- ✅ Calculation history storage
- ⚠️ Requires PostgreSQL installation

#### CLI Calculator
```bash
# Run the calculator demo
uv run python -m codespace_learning.main

# Run tests
uv run --extra dev python -m pytest tests/ -v

# Run with coverage
uv run --extra dev python -m pytest tests/ --cov=codespace_learning
```

### GitHub Codespaces Development

#### Automatic Startup (Recommended)
When you open the Codespace, everything is configured automatically:
- PostgreSQL database server starts in a Docker container
- Python environment is set up with all dependencies
- FastAPI server starts automatically on port 8000

**Access Points (automatically forwarded):**
- **API Documentation**: http://localhost:8000/docs (Interactive Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc  
- **API Root**: http://localhost:8000
- **Health Check**: http://localhost:8000/health

#### Manual Commands (if needed)
```bash
# Start the API server manually
./scripts/start_api.sh

# Or start simple API (no database)
./scripts/start_simple_api.sh

# Test database connection
psql postgresql://postgres:postgres@db/calculator_db -c "SELECT version();"
```

#### DevContainer Architecture
The Codespace uses Docker Compose with two services:
- **app**: Python 3.13 environment with your code
- **db**: PostgreSQL 15 database with persistent storage

Environment variables are automatically set:
- `DATABASE_URL=postgresql+psycopg://postgres:postgres@db/calculator_db`

## 🔧 DevContainer Features

This project demonstrates modern DevContainer concepts using Docker Compose:

### Multi-Container Architecture
- **App Container**: Custom Python 3.13 environment with development tools
- **Database Container**: PostgreSQL 15 with persistent volume storage
- **Service Communication**: Containers communicate via Docker network

### Base Configuration
- **Custom Dockerfile**: Python 3.13 on Debian Bullseye
- **PostgreSQL Client**: Pre-installed for database operations
- **Development Tools**: uv, llm, and GitHub Models integration

### Features Added via DevContainer
- **Node.js LTS** - For frontend tooling if needed
- **GitHub CLI** - Direct GitHub integration
- **Docker-in-Docker** - Container support within container

### VS Code Extensions
- Python language support with Pylance
- GitHub Copilot for AI assistance  
- Black formatter and isort for code formatting
- Python environment management

### Post-Create Commands
- Installs dependencies with `uv sync`
- Sets up `llm` tool with GitHub Models integration
- Configures GPT-4o as default model for free AI assistance
- Database is automatically available via Docker Compose

### Key Learning: Why Docker Compose?
The postgres DevContainer "feature" only installs client tools, not a database server. Docker Compose provides:
- ✅ Real PostgreSQL server in separate container
- ✅ Persistent data storage
- ✅ Proper service isolation
- ✅ Production-like architecture

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

### PostgreSQL Setup (Docker Compose)
- **PostgreSQL 15** runs in separate container service named `db`
- **Persistent Volume**: `postgres-data` preserves data between Codespace restarts
- **Automatic Startup**: Database starts when Codespace opens
- **Connection**: App connects via service name, not localhost

### Database Features
- **Calculation History**: All API operations stored permanently  
- **SQLAlchemy ORM**: Modern Python database operations
- **Automatic Tables**: Created on first API startup
- **Environment Config**: `DATABASE_URL` automatically set

### Connection Details
```bash
Host: db (service name in Docker Compose)
Port: 5432 (default PostgreSQL)
Database: calculator_db
Username: postgres
Password: postgres
Full URL: postgresql+psycopg://postgres:postgres@db/calculator_db
```

## 🎓 Learning Concepts

### 1. **DevContainer Configuration**
The `.devcontainer/` folder contains:
- **devcontainer.json**: Main configuration pointing to Docker Compose
- **docker-compose.yml**: Multi-container setup (app + database)
- **Dockerfile**: Custom Python environment with tools
- **Port Forwarding**: Automatically forwards ports 8000 and 5432

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

## 🔧 Troubleshooting Codespaces

### Common Issues and Solutions

#### 1. Containers Not Starting / Database Issues
```bash
# Check overall DevContainer status
./scripts/check_devcontainer.sh

# In DevContainers, you DON'T manually start containers
# The database service runs automatically alongside your app container

# If database isn't working, rebuild the DevContainer:
# VS Code Command Palette (Cmd/Ctrl+Shift+P) → "Rebuild Container"
```

#### 2. Database Connection Issues
```bash
# Test connection directly
psql postgresql://postgres:postgres@db/calculator_db -c "SELECT version();"

# If connection fails, wait a moment (database might still be starting)
sleep 10 && psql postgresql://postgres:postgres@db/calculator_db -c "\l"

# The calculator_db database is created automatically
# If it doesn't exist, the startup script will create it
```

#### 3. API Server Won't Start
```bash
# Check dependencies
uv sync

# Install postgres extras
uv pip install -e ".[postgres]"

# Start with debug info
uv run python -c "from codespace_learning.app import app; print('App imported successfully')"
```

#### 4. Port Forwarding Issues
- Codespaces should automatically forward ports 8000 and 5432
- If not working: Go to "Ports" tab in VS Code and manually add ports
- Make sure visibility is set to "Public" if sharing with others

### Reset Everything
If nothing works, rebuild completely:
1. VS Code → Command Palette → "Codespaces: Rebuild Container"
2. Wait for full rebuild (3-5 minutes)
3. Run `./scripts/start_api.sh`

## 🔗 Useful Links

- **Direct Codespace**: `https://codespaces.new/deepaks7n/codespace-learning?quickstart=1`
- **GitHub Codespaces Docs**: https://docs.github.com/en/codespaces
- **DevContainer Spec**: https://containers.dev/
- **Available Images**: https://github.com/devcontainers/images
- **Available Features**: https://github.com/devcontainers/features
- **Docker Compose DevContainers**: https://code.visualstudio.com/docs/devcontainers/docker-compose