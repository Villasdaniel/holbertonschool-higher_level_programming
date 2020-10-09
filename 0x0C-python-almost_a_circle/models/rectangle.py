#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validation(name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set with"""
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """height"""
        return self.__x

    @x.setter
    def x(self, value):
        """set height"""
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """height"""
        return self.__y

    @y.setter
    def y(self, value):
        """set height"""
        self.validation("y", value)
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print rectangle"""
        print("\n" * self.__y, end="")
        for a in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Print string with data"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """update the values"""
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)
        elif args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
