FROM mcr.microsoft.com/devcontainers/python:3.13-bullseye

# Install additional system packages
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Install llm and configure GitHub models
RUN pip install llm llm-github-models