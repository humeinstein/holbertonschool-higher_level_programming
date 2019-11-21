#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Tests for Max Integer
    """
    def test_neg(self):
        """testcase"""
        test_list = [1, 5, 10, -1, -50, -100, 100]
        self.assertEqual(max_int(test_list), 8)

    def max_integer(self):
        """ test for empty """
        self.assertEqual(max_int([]), None)