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

    def test_tuple(self):
        """random"""
        with self.assertRaises(TypeError):
            _max = max_integer((2, 3))

    def test_None(self):
        """random"""
        with self.assertRaises(TypeError):
            _max = max_integer(None)

    def test_big_number(self):
        """big numbers"""
        _list = [2135456413213546541321324163463123132746,
                 13524654351321324135461321354]
        self.assertEqual(max_integer(_list),
                         2135456413213546541321324163463123132746)

    def test_float(self):
        """floats"""
        _list = [2.3, 5.6, 7.8]
        with self.assertRaises(TypeError):
            _max = max_integer(_list)

    def test_inf(self):
        _list = [float('inf'), float('inf')]
        with self.assertRaises(TypeError):
            _max = max_integer(_list)

    def test_docstringmod(self):
        """comments"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(m is not None and len(m) > 0)

    def test_docstringfunc(self):
        """comments"""
        f = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(f is not None and len(f) > 5)

    def test_morethan(self):
        """ones"""
        with self.assertRaises(TypeError):
            _max = max_integer(1, 1)

if __name__ == '__main__':
    unittest.main()
