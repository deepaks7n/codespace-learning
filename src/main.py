#!/usr/bin/env python3
"""
Main application demonstrating the calculator functions
"""

from calculator import add, subtract, multiply, divide, power, calculate_average


def main():
    """Demonstrate calculator functions"""
    print("🧮 Simple Calculator Demo")
    print("=" * 30)
    
    # Basic operations
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    
    # Average calculation
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    avg = calculate_average(numbers)
    print(f"Average of {numbers} = {avg}")
    
    print("\n✅ Calculator demo completed!")


if __name__ == "__main__":
    main()