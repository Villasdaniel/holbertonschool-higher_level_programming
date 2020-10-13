#!/usr/bin/python3
"""unittest base"""

import unittest
from models.base import Base, __doc__ as mrdoc
import inspect
import pep8


class test_base(unittest.TestCase):
    """unittest base"""
    def test_doctstring(self):
        """Test documentation"""
        print(mrdoc)
        self.assertTrue(len(mrdoc.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_pep8(self):
        """Test PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

if __name__ == "__main__":
    unittest.main()
