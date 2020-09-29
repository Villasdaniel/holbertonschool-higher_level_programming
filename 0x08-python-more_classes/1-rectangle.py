#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
        """
        class Rectangle
        """
        def __init__(self, width=0, height=0):
                """initialize instances"""
                self.__widht = width
                self.__height = height

        @property
        def width(self):
                """return width"""
                return self.__width

        @width.setter
        def width(self, value):
                """width set"""
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                else:
                        self.__width = value

        @property
        def height(self):
                """return height"""
                return self.__height

        @height.setter
        def height(self, value):
                """height set"""
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                else:
                        self.__height = value
