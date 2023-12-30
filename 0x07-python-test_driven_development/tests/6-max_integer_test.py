#!/usr/bin/python3
"""
Unittest for max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """
    test python3 -m unittest -v tests.6-max_integer_test
    """
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, -2, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 5, -2, 4]), 5)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 5, 5, 4]), 5)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

if __name__ == '__main__':
    unittest.main()
