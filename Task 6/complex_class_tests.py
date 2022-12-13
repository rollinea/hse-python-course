import unittest

from complex_class import Complex


class TestComplex(unittest.TestCase):

    def test_equal(self):
        first = Complex(1, 1)
        second = Complex(1, 1)
        third = Complex(2, 2)
        self.assertTrue(first == second)
        self.assertFalse(second == third)

    def test_add(self):
        first = Complex(2, 3)
        second = Complex(1, 0)
        third = Complex(2, 3)
        self.assertEqual(first.add(second), Complex(3, 3))
        self.assertNotEqual(first.add(third), Complex(1, 1))

    def test_subtract(self):
        first = Complex(5, 5)
        second = Complex(2, 3)
        third = Complex(0, 1)
        self.assertEqual(first.subtract(second), Complex(3, 2))
        self.assertEqual(third.subtract(second), Complex(-2, -2))

    def test_multiply(self):
        first = Complex(1, 1)
        second = Complex(0, 3)
        third = Complex(0, 0)
        self.assertEqual(first.multiply(second), Complex(-3, 3))
        self.assertEqual(first.multiply(third), Complex(0, 0))

    def test_divide(self):
        first = Complex(-2, 1)
        second = Complex(1, -1)
        third = Complex(0, 0)
        self.assertEqual(first.divide(second), Complex(-1.5, -0.5))
        self.assertEqual(first.divide(third), 'Divide by zero!')

    def test_length(self):
        first = Complex(3, 4)
        second = Complex(0, 3.5)
        self.assertEqual(first.length(), 5)
        self.assertEqual(second.length(), 3.5)
