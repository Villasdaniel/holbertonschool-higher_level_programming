#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns the number of characters"""


def write_file(filename="", text=""):
        """writes a string to a text file (UTF8) and returns the number of characters"""
        with open(filename, 'w', encoding="utf-8") as f:
                return(f.write(text))
