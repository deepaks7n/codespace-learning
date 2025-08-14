"""Database models for calculations."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from src.database.connection import Base


class Calculation(Base):
    """Database model for storing calculation history."""
    
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    operand1 = Column(Float)
    operand2 = Column(Float, nullable=True)  # Some operations only need one operand
    operands_list = Column(String, nullable=True)  # For operations like average/median
    result = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Calculation(id={self.id}, operation='{self.operation}', result={self.result})>"