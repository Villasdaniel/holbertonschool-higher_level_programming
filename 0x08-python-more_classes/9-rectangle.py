#!/usr/bin/python3
"""class square"""


class Rectangle:
        """
        class square
        """
        number_of_instances = 0
        print_symbol = '#'
        def __init__(self, width=0, height=0):
                self.__width = width
                self.__height = height
                Rectangle.number_of_instances += 1
                
        @property
        def width(self):
                return self.__width

        @width.setter
        def width(self, value):
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                else:
                        self.__width = value
        
        @property
        def height(self):
                return self.__height
        
        @height.setter
        def height(self, value):
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                else:
                        self.__height = value
        
        def area(self):
                """method return current rectangle area"""
                return (self.__width * self.__height)
        
        def perimeter(self):
                """method return current rectangle perimeter"""
                if (self.__width == 0) or (self.__height == 0):
                        return 0
                return((self.__width * 2) + (self.__height * 2))

        def __str__(self):
                if self.__width == 0 or self.__height == 0:
                        return("")
                return ((str(self.print_symbol) * self.__width + '\n') * self.__height)[:-1]

        def __repr__(self):
                return ('Rectangle({}, {})'.format(self.__width, self.__height))

        def __del__(self):
                print("Bye rectangle...")
                Rectangle.number_of_instances -= 1

        @staticmethod
        def bigger_or_equal(rect_1, rect_2):
                if (isinstance(rect_1, Rectangle) == False):
                        raise TypeError("rect_1 must be an instance of Rectangle")
                if (isinstance(rect_2, Rectangle) == False):
                        raise TypeError("rect_2 must be an instance of Rectangle")
                if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
                        return rect_1
        
        @classmethod
        def square(cls, size=0):
                return cls(size, size)