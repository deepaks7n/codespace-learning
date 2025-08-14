"""Calculator API endpoints."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.models.calculation import Calculation
from src.models.schemas import (
    BasicOperationRequest,
    SingleOperandRequest,
    PercentageRequest,
    ListOperationRequest,
    CalculationResponse,
    ErrorResponse,
)
from src import calculator

router = APIRouter(prefix="/calculator", tags=["Calculator"])


def save_calculation(
    db: Session,
    operation: str,
    result: float,
    operand1: float = None,
    operand2: float = None,
    operands_list: str = None,
) -> Calculation:
    """Save calculation to database."""
    db_calculation = Calculation(
        operation=operation,
        operand1=operand1,
        operand2=operand2,
        operands_list=operands_list,
        result=result,
    )
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation


@router.post("/add", response_model=CalculationResponse)
async def add_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Add two numbers."""
    try:
        result = calculator.add(request.operand1, request.operand2)
        calculation = save_calculation(
            db, "add", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/subtract", response_model=CalculationResponse)
async def subtract_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Subtract two numbers."""
    try:
        result = calculator.subtract(request.operand1, request.operand2)
        calculation = save_calculation(
            db, "subtract", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/multiply", response_model=CalculationResponse)
async def multiply_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Multiply two numbers."""
    try:
        result = calculator.multiply(request.operand1, request.operand2)
        calculation = save_calculation(
            db, "multiply", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/divide", response_model=CalculationResponse)
async def divide_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Divide two numbers."""
    try:
        result = calculator.divide(request.operand1, request.operand2)
        calculation = save_calculation(
            db, "divide", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/power", response_model=CalculationResponse)
async def power_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Calculate base raised to power."""
    try:
        result = calculator.power(request.operand1, request.operand2)
        calculation = save_calculation(
            db, "power", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/modulo", response_model=CalculationResponse)
async def modulo_numbers(request: BasicOperationRequest, db: Session = Depends(get_db)):
    """Calculate modulo operation."""
    try:
        result = calculator.modulo(int(request.operand1), int(request.operand2))
        calculation = save_calculation(
            db, "modulo", result, request.operand1, request.operand2
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sqrt", response_model=CalculationResponse)
async def sqrt_number(request: SingleOperandRequest, db: Session = Depends(get_db)):
    """Calculate square root."""
    try:
        result = calculator.sqrt(request.operand)
        calculation = save_calculation(db, "sqrt", result, request.operand)
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/factorial", response_model=CalculationResponse)
async def factorial_number(request: SingleOperandRequest, db: Session = Depends(get_db)):
    """Calculate factorial."""
    try:
        result = calculator.factorial(int(request.operand))
        calculation = save_calculation(db, "factorial", result, request.operand)
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/percentage", response_model=CalculationResponse)
async def percentage_calculation(
    request: PercentageRequest, db: Session = Depends(get_db)
):
    """Calculate percentage."""
    try:
        result = calculator.percentage(request.part, request.whole)
        calculation = save_calculation(
            db, "percentage", result, request.part, request.whole
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/average", response_model=CalculationResponse)
async def average_calculation(
    request: ListOperationRequest, db: Session = Depends(get_db)
):
    """Calculate average."""
    try:
        result = calculator.calculate_average(request.numbers)
        calculation = save_calculation(
            db, "average", result, operands_list=str(request.numbers)
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/median", response_model=CalculationResponse)
async def median_calculation(
    request: ListOperationRequest, db: Session = Depends(get_db)
):
    """Calculate median."""
    try:
        result = calculator.calculate_median(request.numbers)
        calculation = save_calculation(
            db, "median", result, operands_list=str(request.numbers)
        )
        return calculation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/history", response_model=List[CalculationResponse])
async def get_calculation_history(
    limit: int = 50, db: Session = Depends(get_db)
):
    """Get calculation history."""
    calculations = (
        db.query(Calculation)
        .order_by(Calculation.created_at.desc())
        .limit(limit)
        .all()
    )
    return calculations


@router.get("/history/{calculation_id}", response_model=CalculationResponse)
async def get_calculation(calculation_id: int, db: Session = Depends(get_db)):
    """Get specific calculation by ID."""
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()
    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")
    return calculation