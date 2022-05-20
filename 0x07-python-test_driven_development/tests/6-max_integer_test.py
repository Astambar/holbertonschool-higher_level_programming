#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 5, 4, 7, 0]), 7)

    def test_max_integer_emptyArgs(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_end_list(self):
        self.assertEqual(max_integer([1, 2, 3, 5, 4, 7, 8]), 8)

    def test_max_integer_start_list(self):
        self.assertEqual(max_integer([9, 2, 3, 5, 4, 7, 8]), 9)

    def test_max_integer_letter(self):
        self.assertEqual(max_integer("ZzaA"), 'z')

    def test_max_integer_lenListOne(self):
        self.assertEqual(max_integer([3]), 3)

    def test_max_integer_AllNegative(self):
        self.assertEqual(max_integer([-99, -60, -30, -150]), -30)

    def test_max_integer_NegativeIsPresent(self):
        self.assertEqual(max_integer([-99, 100, 50, -10]), 100)

    def test_max_integer_NegativeIsLogicalComportment(self):
        self.assertEqual(max_integer([-101, 100, 50, -10]), 100)

    def test_max_integger_ArgsIsNone(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_integger_listIsString(self):
        with self.assertRaises(TypeError):
            max_integer([98, -33, 64, "ZzaA", 90, 32, 30])

    def test_max_integger_ArgsIsInteger(self):
        with self.assertRaises(TypeError):
            max_integer(51)

    def test_max_integger_listIsFloat(self):
        self.assertEqual(max_integer([51.27, 36.3036, 41.7]), 51.27)


if __name__ == "__main__":
    unittest.main()
