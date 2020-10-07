#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
        """reads a text file (UTF8) and prints it to stdout"""
        with open(filename, encoding="utf-8") as f:
                if nb_lines <= 0:
                        print(f.read(), end="")
                else:
                        i = 0
                        while i < nb_lines:
                                print(f.readline(), end="")
                                i += 1
