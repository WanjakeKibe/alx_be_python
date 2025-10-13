import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Test zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 15), -5)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        
        # Test zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(1.5, 2.5), -1.0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
        # Test identity property
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        
        # Test decimal results
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 4), 0.25)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        # Test division by one
        self.assertEqual(self.calc.divide(7, 1), 7)
        self.assertEqual(self.calc.divide(-3, 1), -3)
        
        # Test zero divided by non-zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    # Run the tests
    unittest.main()