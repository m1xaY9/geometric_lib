import unittest

from rectangle import area, perimeter

class TestAreaAndPerimeter(unittest.TestCase):

    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_area_small_input(self):
        res = area(3, 2)
        self.assertEqual(res, 6)
    def test_area_big_input(self):
        res = area(123456789, 123456789)
        self.assertEqual(res, 123456789 * 123456789)

    def test_area_negative(self):
        self.assertRaises(ValueError, area, -3, 2)

    def test_area_string(self):
        self.assertRaises(TypeError, area, "one", "two")
    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_perimeter_small_input(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)
    def test_perimeter_big_input(self):
        res = perimeter(123456789, 123456789)
        self.assertEqual(res, 2*(123456789 + 123456789))

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter, -3, -2)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "one", "two")
