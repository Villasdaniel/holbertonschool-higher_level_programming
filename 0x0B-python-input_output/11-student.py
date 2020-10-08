#!/usr/bin/python3
"""class Student that defines a student"""


class Student():
        """class student"""
        def __init__(first_name, last_name, age):
                """init student"""
                self.first_name = first_name
                self.last_name = last_name
                self.age = age

def to_json(self):
        """returns the dictionary description"""
        return self.__dict__
