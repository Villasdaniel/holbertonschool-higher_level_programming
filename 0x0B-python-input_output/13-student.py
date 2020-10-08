#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description"""
        mydic = {}
        if type(attrs) is list:
            for obj in attrs:
                if type(obj) is str and obj in self.__dict__.keys():
                    mydic[obj] = self.__dict__[obj]
            return mydic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        if json:
            self.__dic__ = json
