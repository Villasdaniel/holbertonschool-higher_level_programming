#!/usr/bin/python3
"""first class"""


class Square:
        """(python3 -c 'print(__import__("my_module").MyClass.__doc__)')
        """
        def __init__(self, size=0):
                """variable initializing"""
                self.__size = size
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
