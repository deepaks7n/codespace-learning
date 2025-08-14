"""
Unit tests for calculator functions
"""

import unittest
from codespace_learning.calculator import (
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


class TestCalculator(unittest.TestCase):

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self) -> None:
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)

        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self) -> None:
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)

    def test_calculate_average(self) -> None:
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10]), 10.0)

        with self.assertRaises(ValueError):
            calculate_average([])

    def test_modulo(self) -> None:
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(9, 3), 0)
        with self.assertRaises(ValueError):
            modulo(1, 0)

    def test_sqrt(self) -> None:
        self.assertEqual(sqrt(16), 4.0)
        self.assertEqual(sqrt(2.25), 1.5)
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_factorial(self) -> None:
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(3.5)  # type: ignore[arg-type]

    def test_percentage(self) -> None:
        self.assertAlmostEqual(percentage(25, 200), 12.5)
        self.assertAlmostEqual(percentage(1, 4), 25.0)
        with self.assertRaises(ValueError):
            percentage(1, 0)

    def test_median(self) -> None:
        self.assertEqual(calculate_median([1, 3, 3, 6, 7, 8, 9]), 6.0)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)
        with self.assertRaises(ValueError):
            calculate_median([])


if __name__ == "__main__":
    unittest.main()
