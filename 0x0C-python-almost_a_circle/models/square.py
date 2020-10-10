#!/usr/bin/python3
"""square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """width"""
        return self.width

    @size.setter
    def size(self, value):
        """set with"""
        self.width = value
        self.height = value

    def __str__(self):
        """Print string with data"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.size))

    def update(self, *args, **kwargs):
        """update the values"""
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)
        elif args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        a = {}
        for key in ["id", "size", "x", "y"]:
            a[key] = getattr(self, key)
        return a
