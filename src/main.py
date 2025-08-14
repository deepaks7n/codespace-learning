#!/usr/bin/env python3
"""
Main application demonstrating the calculator functions
"""

from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    sqrt,
    factorial,
    percentage,
    calculate_average,
    calculate_median,
)


def main() -> None:
    """Demonstrate calculator functions"""
    print("🧮 Simple Calculator Demo")
    print("=" * 30)

    # Basic operations
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")

    # Extra operations
    print(f"10 % 3 = {modulo(10, 3)}")
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"5! = {factorial(5)}")
    print(f"25 as % of 200 = {percentage(25, 200)}%")

    # Average/median calculation
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    avg = calculate_average(numbers)
    med = calculate_median(numbers)
    print(f"Average of {numbers} = {avg}")
    print(f"Median of {numbers} = {med}")

    print("\n✅ Calculator demo completed!")


if __name__ == "__main__":
    main()
