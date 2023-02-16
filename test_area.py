import unittest
from compute_area import circle_area
from math import pi

class TestAreaFunction(unittest.TestCase):
    def test_area(self):
        # Test radius when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi* 2.1**2)

    def test_values(self):
        # See if we get value error on negative numbers
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # see whether it raises when given non real integers
        self.assertRaises(TypeError, circle_area, "radius")
        self.assertRaises(TypeError, circle_area, 2 + 5j)
        self.assertRaises(TypeError, circle_area, True)