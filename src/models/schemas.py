"""Pydantic schemas for API requests and responses."""

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel

Number = Union[int, float]


class CalculationRequest(BaseModel):
    """Base request for calculations."""
    operation: str


class BasicOperationRequest(CalculationRequest):
    """Request for basic operations (add, subtract, multiply, divide, power, modulo)."""
    operand1: Number
    operand2: Number


class SingleOperandRequest(CalculationRequest):
    """Request for single operand operations (sqrt, factorial)."""
    operand: Number


class PercentageRequest(CalculationRequest):
    """Request for percentage calculation."""
    part: Number
    whole: Number


class ListOperationRequest(CalculationRequest):
    """Request for list operations (average, median)."""
    numbers: List[Number]


class CalculationResponse(BaseModel):
    """Response for calculation results."""
    id: int
    operation: str
    operand1: Optional[Number] = None
    operand2: Optional[Number] = None
    operands_list: Optional[str] = None
    result: Number
    created_at: datetime

    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    detail: Optional[str] = None