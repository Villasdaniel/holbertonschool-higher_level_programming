#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :


"""


def text_indentation(text):
        """
        prints a text with 2 new lines after characters: ., ? and :
        """
        if type(text) is not str:
                raise TypeError("text must be a string")
        
        text = text.replace('.', '.\n\n')
        text = text.replace('?', '?\n\n')
        text = text.replace(':', ':\n\n')
        print("\n".join(i.strip() for i in text.split("\n")), end="")
