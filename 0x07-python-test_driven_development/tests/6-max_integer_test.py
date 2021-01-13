#!/usr/bin/python3
"""Unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """testing for max integer in list func"""

    def test_for_max_int(self):
        """tests successful cases of max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)
        self.assertEqual(max_integer([-10, -20, -30]), -10)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

    def test_errors(self):
        """tests errors raised by incorrect type arguments"""
        self.assertRaises(Exception, max_integer, ["string", 3])

    def test_empty(self):
        """tests errors if argument is none"""
        self.assertIsNone(max_integer())

