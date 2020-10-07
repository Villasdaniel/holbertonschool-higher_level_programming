#!/usr/bin/python3
"""[summary]"""


def read_file(filename=""):
        """reads a text file and prints it to stdout"""
        with open('my_file_0.txt', 'r') as f:
                print(f.read())
