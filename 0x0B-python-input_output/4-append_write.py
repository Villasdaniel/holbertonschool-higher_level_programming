#!/usr/bin/python3
"""appends and returns the number of characters added"""


def append_write(filename="", text=""):
        """appends and returns the number of characters added"""
        with open(filename, 'a', encoding="utf-8") as f:
                return(f.write(text))
