#!/usr/bin/python3
"""[summary]"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
        """empty class
        """
        def __init__(self, size):
                """[summary]"""
                self.integer_validator('size', size)
                self.__size = size
                super().__init__(size, size)

        def area(self):
                """area function"""
                return self.__size * self.__size
