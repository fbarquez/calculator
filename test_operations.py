
import unittest
from operations import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_zero(self):
        self.assertEqual(divide(10, 0), "Error: Division by zero")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(-1), "Error")

    def test_square_root_negative(self):
        self.assertEqual(square_root(-9), "Error")

    def test_percentage(self):
        self.assertEqual(percentage(200, 10), 20)

    def test_modulo_zero(self):
        self.assertEqual(modulo(10, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()
