#!/usr/bin/python3
"""first class"""


class Square:
        """(python3 -c 'print(__import__("my_module").MyClass.__doc__)')
        """
        def __init__(self, size=0):
                """variable initializing"""
                self.__size = size

        @property
        def size(self):
                """return value of size"""
                return self.__size

        @size.setter
        def size(self, size):
                """variable initializing"""
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        def area(self):
                """method return current square area"""
                return (self.__size * self.__size)

        def my_print(self):
                """method to print # in all the square position"""
                for i in range(self.__size):
                        print("#" * self.__size)
                if self.__size == 0:
                        print()
