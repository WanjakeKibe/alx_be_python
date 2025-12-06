# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test Addition Method
    def test_addition_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertEqual(self.calc.add(3, -7), -4)

    def test_addition_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_decimal_numbers(self):
        """Test addition with decimal numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)
        self.assertEqual(self.calc.add(-2.5, 1.5), -1.0)

    # Test Subtraction Method
    def test_subtraction_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(100, 25), 75)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 10), -15)
        self.assertEqual(self.calc.subtract(3, -7), 10)

    def test_subtraction_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_decimal_numbers(self):
        """Test subtraction with decimal numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(2.2, 1.1), 1.1)
        self.assertEqual(self.calc.subtract(-2.5, 1.5), -4.0)

    # Test Multiplication Method
    def test_multiplication_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(7, 8), 56)

    def test_multiplication_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_decimal_numbers(self):
        """Test multiplication with decimal numbers."""
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.5), 3.75)
        self.assertEqual(self.calc.multiply(-2.5, 2), -5.0)

    # Test Division Method
    def test_division_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

    def test_division_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_division_decimal_numbers(self):
        """Test division with decimal numbers."""
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertEqual(self.calc.divide(2.2, 1.1), 2.0)
        self.assertEqual(self.calc.divide(1.0, 4.0), 0.25)

    def test_division_by_zero(self):
        """Test division by zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_division_zero_numerator(self):
        """Test division with zero as numerator."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    # Test Edge Cases
    def test_large_numbers(self):
        """Test operations with large numbers."""
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        self.assertEqual(self.calc.divide(1000000, 2), 500000.0)

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        self.assertEqual(self.calc.add(0.0001, 0.0002), 0.0003)
        self.assertEqual(self.calc.multiply(0.1, 0.1), 0.01)

    # Test Type Consistency
    def test_return_types(self):
        """Test that methods return correct types."""
        self.assertIsInstance(self.calc.add(1, 2), (int, float))
        self.assertIsInstance(self.calc.subtract(1, 2), (int, float))
        self.assertIsInstance(self.calc.multiply(1, 2), (int, float))
        self.assertIsInstance(self.calc.divide(1, 2), (int, float))

    # Test that division by zero returns None
    def test_division_by_zero_type(self):
        """Test that division by zero returns None (not an error)."""
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    # Run the tests
    unittest.main()
