#!/usr/bin/python3
"""unittest base"""

import unittest
from models.base import Base
import inspect
import pep8


class test_base(unittest.TestCase):
    """unittest base"""
    def test_doctstring(self):
        """Test documentation"""
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__.strip()) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.create.__doc__.strip()) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__.strip()) > 0)

    def test_pep8(self):
        """Test PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

if __name__ == "__main__":
    unittest.main()
