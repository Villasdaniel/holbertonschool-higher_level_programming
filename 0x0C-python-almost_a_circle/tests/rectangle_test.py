#!/usr/bin/python3
"""unittest rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import inspect
import pep8


class base_test(unittest, testcase):
"""unittest rectangle"""
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
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0)

	def test_rectangle_success(self):
		"""check success class work"""
		R = Rectangle(1, 2)
		self.assertEqual(R.width, 1)
		self.assertEqual(R.height, 2)
		self.assertEqual(R.x, 0)
		self.assertEqual(R.y, 0)

	def test_instances(self):
		"""check instances"""
		with self.assertRaises(TypeError):
			R = Rectangle()
		with self.assertRaises(TypeError):
			R = Rectangle(1)
		with self.assertRaises(TypeError):
			R = Rectangle(1,2,3,4,5,6)
		with self.assertRaises(ValueError):
			R = Rectangle(0, 1)
		with self.assertRaises(ValueError):
			R = Rectangle(1, 0)

if __name__ == "__main__":
    unittest.main()
