"""
Tests for the Calculator API
"""

import pytest
from fastapi.testclient import TestClient
from codespace_learning.app import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns API information."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Calculator API"


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_add_endpoint():
    """Test the add operation endpoint."""
    response = client.post(
        "/calculator/add",
        json={"operation": "add", "operand1": 10, "operand2": 5}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 15
    assert data["operation"] == "add"
    assert data["operand1"] == 10
    assert data["operand2"] == 5


def test_sqrt_endpoint():
    """Test the square root operation endpoint."""
    response = client.post(
        "/calculator/sqrt",
        json={"operation": "sqrt", "operand": 16}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 4.0
    assert data["operation"] == "sqrt"
    assert data["operand1"] == 16


def test_divide_by_zero():
    """Test divide by zero error handling."""
    response = client.post(
        "/calculator/divide",
        json={"operation": "divide", "operand1": 10, "operand2": 0}
    )
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json()["detail"]


def test_average_endpoint():
    """Test the average calculation endpoint."""
    response = client.post(
        "/calculator/average",
        json={"operation": "average", "numbers": [1, 2, 3, 4, 5]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 3.0
    assert data["operation"] == "average"


def test_history_endpoint():
    """Test the calculation history endpoint."""
    # First make a calculation
    client.post(
        "/calculator/add",
        json={"operation": "add", "operand1": 1, "operand2": 1}
    )
    
    # Then check history
    response = client.get("/calculator/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0