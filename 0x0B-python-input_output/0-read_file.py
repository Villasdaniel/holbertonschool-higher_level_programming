#!/usr/bin/python3
"""[summary]"""


def read_file(filename=""):
        """reads a text file (UTF8) and prints it to stdout:"""
        with open('my_file_0.txt', 'r') as f:
                read_data = f.read()
                print("{}".format(read_data))
