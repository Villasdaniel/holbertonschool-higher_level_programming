#!/usr/bin/python3
"""returns the number of lines of a text file"""


def number_of_lines(filename=""):
        """returns the number of lines of a text file"""


        with open(filename, 'r') as f:
                return(sum(1 for line in f))
