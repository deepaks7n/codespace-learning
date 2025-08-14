# GitHub Codespaces Learning Project

A simple Python calculator project designed to learn GitHub Codespaces and DevContainers.

## 🎯 Learning Objectives

- Understand GitHub Codespaces configuration
- Learn DevContainer setup and customization  
- Practice with VS Code extensions in containers
- Explore automated development environment setup

## 🚀 Quick Start with Codespaces

1. **Launch Codespace**: Click the green "Code" button and select "Create codespace on main"
2. **Or use direct link**: `https://codespaces.new/deepaks7n/codespace-learning?quickstart=1`

## 📁 Project Structure

```
├── .devcontainer/
│   └── devcontainer.json     # Codespace configuration
├── src/
│   ├── __init__.py
│   ├── calculator.py         # Calculator functions
│   └── main.py              # Main application
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Unit tests
├── requirements.txt          # Development dependencies
├── pyproject.toml           # Project configuration
└── README.md
```

## 🧮 Running the Calculator

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

### VS Code Extensions
- Python language support with Pylance
- GitHub Copilot for AI assistance  
- Black formatter and isort for code formatting
- Python environment management

### Post-Create Commands
- Installs `uv` for fast Python package management
- Sets up `llm` tool with GitHub Models integration
- Configures GPT-4o as default model for free AI assistance

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