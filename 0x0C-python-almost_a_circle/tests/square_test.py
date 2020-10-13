#!/usr/bin/python3
"""unittest square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import inspect
import pep8


class base_test(unittest, testcase):
"""unittest square"""
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
        """ Test PEP-8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.assertEqual(result.total_errors, 0)

	def test_square_success(self):
		"""check success class work"""
		S = Square(1)
		self.assertEqual(S.size, 1)
		self.assertEqual(S.x, 0)
		self.assertEqual(S.y, 0)

	def test_instances(self):
		"""check instances"""
		with self.assertRaises(TypeError):
			S = Square()
		with self.assertRaises(TypeError):
			S = Square(1,2,3,4,5,6)
		with self.assertRaises(ValueError):
			S = Square(0)

if __name__ == "__main__":
    unittest.main()
