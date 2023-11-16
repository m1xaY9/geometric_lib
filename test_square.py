import unittest

from square import area
from square import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_small_input(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_area_big_input(self):
        res = area(123456789000)
        self.assertEqual(res, 123456789000 * 123456789000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_small_input(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_perimeter_big_input(self):
        res = perimeter(123456789000)
        self.assertEqual(res, 2*(123456789000 + 123456789000))
