"""
Simple calculator functions for learning GitHub Codespaces and DevContainers.

This module intentionally keeps a small, easy-to-understand API while also
showcasing a few additional, commonly-used operations with helpful error
handling and type hints.
"""

from __future__ import annotations

from math import sqrt as _sqrt
from typing import Sequence, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Divide two numbers.

    Raises
    ------
    ValueError
        If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a: int, b: int) -> int:
    """Return ``a % b``.

    Raises
    ------
    ValueError
        If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def power(base: Number, exponent: Number) -> Number:
    """Calculate base raised to the power of exponent."""
    return base ** exponent


def sqrt(n: Number) -> float:
    """Square root of ``n``.

    Raises
    ------
    ValueError
        If ``n`` is negative.
    """
    # Explicit float cast ensures support for both int and float while
    # allowing comparison
    if float(n) < 0.0:
        raise ValueError("Cannot take square root of a negative number")
    n_float = float(n)
    if n_float < 0.0:
        raise ValueError("Cannot take square root of a negative number")
    return float(_sqrt(n_float))


def factorial(n: int) -> int:
    """Return n! for a non-negative integer ``n``.

    Raises
    ------
    ValueError
        If ``n`` is negative or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("factorial() only accepts integers")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def percentage(part: Number, whole: Number) -> float:
    """Return ``part`` as a percentage of ``whole``.

    Example: percentage(25, 200) -> 12.5

    Raises
    ------
    ValueError
        If ``whole`` is zero.
    """
    if whole == 0:
        raise ValueError("Cannot compute percentage with a zero whole")
    return float(part) / float(whole) * 100.0


def calculate_average(numbers: Sequence[Number]) -> float:
    """Calculate the average (mean) of a list of numbers.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def calculate_median(numbers: Sequence[Number]) -> float:
    """Calculate the median of a list of numbers.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_nums = sorted(float(n) for n in numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
