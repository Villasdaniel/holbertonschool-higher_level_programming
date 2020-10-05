#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        if (value != None):
                for i in a_dictionary:
                        if (value == i[0]):
                                a_dictionary.pop(i[0])
                return a_dictionary
