#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """ prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """[summary]"""
        print(sorted(self))
