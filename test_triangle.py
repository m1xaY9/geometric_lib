import unittest
from triangle import area
from triangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_small_input(self):
        res = area(2, 3)
        self.assertEqual(res, 3)

    def test_area_big_input(self):
        res = area(123456789000, 123456789)
        self.assertEqual(res, 123456789000*123456789/2)

    def test_area_negative(self):
        self.assertRaises(ValueError, area, -2, 3)

    def test_area_string(self):
        self.assertRaises(TypeError, area, "one", "two")

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_small_input(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_perimeter_big_input(self):
        res = perimeter(123456789000, 123456789000, 123456789000)
        self.assertEqual(res, 123456789000 + 123456789000 + 123456789000)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter, -3, -2, -4)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "one", "two", "one")
