#!/usr/bin/python3
"""
Function that addintegers


"""


def add_integer(a, b=98):
    """add two integers

    Args:
        a (int, float): [an integer]
        b (int, optional): [an integer]. Defaults to 98.

    Raises:
        TypeError: [if not an integer or float]
        TypeError: [if not an integer or float]

    Returns:
        [type]: [the add of two integers]
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
