#!/usr/bin/python3
"""[summary]"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
        """empty class
        """
        def __init__(self, width, height):
                """[summary]"""
                self.integer_validator('width', width)
                self.integer_validator('height', height)
                self.__width = width
                self.__height = height

        def area(self):
                """area function"""
                return self.__height * self.__width

        def __str__(self):
                """[summary]"""
                return "[Rectangle] {}/{}".format(self.__width, self.__height)
