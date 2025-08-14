"""FastAPI application for Calculator API (without database)."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union

from .models.schemas import (
    BasicOperationRequest,
    SingleOperandRequest,
    PercentageRequest,
    ListOperationRequest,
    ErrorResponse,
)
from . import calculator

Number = Union[int, float]

app = FastAPI(
    title="Calculator API (Simple)",
    description="A calculator API without database for local development",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple response model without database
class SimpleCalculationResponse:
    def __init__(self, operation: str, result: Number, **kwargs):
        self.operation = operation
        self.result = result
        self.__dict__.update(kwargs)

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Calculator API (Simple)",
        "description": "A learning project for GitHub Codespaces - Local Development Mode",
        "endpoints": {
            "calculator": "/calculator/*",
            "docs": "/docs",
            "openapi": "/openapi.json",
        },
        "note": "Running without database - calculations are not stored"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Calculator API is running (simple mode)"}

@app.post("/calculator/add")
async def add_numbers(request: BasicOperationRequest):
    """Add two numbers."""
    try:
        result = calculator.add(request.operand1, request.operand2)
        return {
            "operation": "add",
            "operand1": request.operand1,
            "operand2": request.operand2,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/subtract")
async def subtract_numbers(request: BasicOperationRequest):
    """Subtract two numbers."""
    try:
        result = calculator.subtract(request.operand1, request.operand2)
        return {
            "operation": "subtract",
            "operand1": request.operand1,
            "operand2": request.operand2,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/multiply")
async def multiply_numbers(request: BasicOperationRequest):
    """Multiply two numbers."""
    try:
        result = calculator.multiply(request.operand1, request.operand2)
        return {
            "operation": "multiply",
            "operand1": request.operand1,
            "operand2": request.operand2,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/divide")
async def divide_numbers(request: BasicOperationRequest):
    """Divide two numbers."""
    try:
        result = calculator.divide(request.operand1, request.operand2)
        return {
            "operation": "divide",
            "operand1": request.operand1,
            "operand2": request.operand2,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/power")
async def power_numbers(request: BasicOperationRequest):
    """Calculate base raised to power."""
    try:
        result = calculator.power(request.operand1, request.operand2)
        return {
            "operation": "power",
            "operand1": request.operand1,
            "operand2": request.operand2,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/sqrt")
async def sqrt_number(request: SingleOperandRequest):
    """Calculate square root."""
    try:
        result = calculator.sqrt(request.operand)
        return {
            "operation": "sqrt",
            "operand": request.operand,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/factorial")
async def factorial_number(request: SingleOperandRequest):
    """Calculate factorial."""
    try:
        result = calculator.factorial(int(request.operand))
        return {
            "operation": "factorial",
            "operand": request.operand,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/percentage")
async def percentage_calculation(request: PercentageRequest):
    """Calculate percentage."""
    try:
        result = calculator.percentage(request.part, request.whole)
        return {
            "operation": "percentage",
            "part": request.part,
            "whole": request.whole,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/average")
async def average_calculation(request: ListOperationRequest):
    """Calculate average."""
    try:
        result = calculator.calculate_average(request.numbers)
        return {
            "operation": "average",
            "numbers": request.numbers,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculator/median")
async def median_calculation(request: ListOperationRequest):
    """Calculate median."""
    try:
        result = calculator.calculate_median(request.numbers)
        return {
            "operation": "median",
            "numbers": request.numbers,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def start_server():
    """Start the simple FastAPI server."""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)