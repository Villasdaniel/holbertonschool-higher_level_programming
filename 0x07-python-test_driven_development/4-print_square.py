#!/usr/bin/python3
"""
Write a function that prints a square with the character #.


"""


def print_square(size):
        """
        Write a function that prints a square with the character #.


        """
        if type(size) not in [int]:
                raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        if type(size) is float and size < 0:
                raise TypeError("size must be an integer")
        for i in range(size):
                for i in range(size):
                        print('#', end='')
                print()
