import unittest
import math
from circle import area
from circle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_small_input(self):
        res = area(3)
        self.assertEqual(res, math.pi * 9)

    def test_area_big_input(self):
        res = area(123456789000)
        self.assertEqual(res, math.pi * 123456789000 * 123456789000)

    def test_area_negative(self):
        res = area(-3)
        self.assertEqual(res, "Радиус не может быть отрицательным числом")

    def test_area_string(self):
        res = area("one", "two")
        self.assertEqual(res, "Радиус не может быть строкой")

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_small_input(self):
        res = perimeter(3)
        self.assertEqual(res, math.pi * 6)

    def test_perimeter_big_input(self):
        res = perimeter(123456789000)
        self.assertEqual(res, 2 * math.pi * 123456789000)

    def test_perimeter_negative(self):
        res = perimeter(-3)
        self.assertEqual(res, "Радиус не может быть отрицательным числом")

    def test_perimeter_string(self):
        res = perimeter("one")
        self.assertEqual(res, "Радиус не может быть строкой")
