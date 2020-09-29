#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """
    class Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize instances"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """method return current rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method return current rectangle perimeter"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return("")
        a = self.print_symbol
        return ((str(a) * self.__width + '\n') * self.__height)[:-1]

    def __repr__(self):
        """Print rectangle data string"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """print a message when delete an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare the instances areas"""
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
