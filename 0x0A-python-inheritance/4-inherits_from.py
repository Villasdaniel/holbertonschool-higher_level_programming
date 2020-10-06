#!/usr/bin/python3
"""[summary]"""


def inherits_from(obj, a_class):
        """True object is an instance of a classinherited,otherwise False"""
        if type(obj) is a_class:
                return False
        return(issubclass(type(obj), a_class))
