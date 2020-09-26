#!/usr/bin/python3
"""
Function that addintegers


"""


def add_integer(a, b=98):
    """
    add two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
