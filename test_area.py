import unittest
from compute_area import circle_area
from math import pi

class TestAreaFunction(unittest.TestCase):
    def test_area(self):
        # Test radius when radius >= 0
        self.assertAlmostEquals(circle_area(1), pi)
        self.assertAlmostEquals(circle_area(0), 0)
        self.assertAlmostEquals(circle_area(2.1), pi*2.1**2)

# if __name__ == '__main__':
#     unittest.main()