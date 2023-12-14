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
        res = area(-3, -2)
        self.assertRaises(res, ValueError)

    def test_area_string(self):
        res = area("one", "two")
        self.assertRaises(res, TypeError)
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
        res = perimeter(-3, -2)
        self.assertRaises(res, ValueError)

    def test_perimeter_string(self):
        res = perimeter("one", "two")
        self.assertRaises(res, TypeError)
