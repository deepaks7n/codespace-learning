"""
Simple calculator functions for learning GitHub Codespaces and DevContainers
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers"""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract two numbers"""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers"""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Calculate base raised to the power of exponent"""
    return base ** exponent


def calculate_average(numbers: list[Number]) -> float:
    """Calculate the average of a list of numbers"""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)