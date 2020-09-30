#!/usr/bin/python3
"""test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        """normal input"""
        self.assertEqual(max_integer([1, 50, 2]), 50)
        self.assertEqual(max_integer([-5, -10, -9]), -5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 4] * 3), 4)

    def test_empty(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)

    def test_None(self):
        """random"""
        with self.assertRaises(TypeError):
            _max = max_integer(None)
