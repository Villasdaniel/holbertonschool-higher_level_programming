#!/usr/bin/python3
"""first class Base"""


import json
import csv


class Base():
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        _list = []
        for obj in list_objs:
            _list.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(Base.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        inslist = []
        try:
            with open(filename, "r") as f:
                pylist = Base.from_json_string(f.read())
            for obj in pylist:
                inslist.append(cls.create(**obj))
            return inslist
        except:
            return inslist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            writecsv = csv.writer(f, delimiter=",")
            if cls.__name__ == "Rectangle":
                keys = ["id", "width", "height", "x", "y"]
            if cls.__name__ == "Square":
                keys = ["id", "size", "x", "y"]
            for obj in list_objs:
                writecsv.writerow(getattr(obj, key) for key in keys)

    @classmethod
    def load_from_file_csv(cls):
        """that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as csv_f:
            csv_reader = csv.DictReader(csv_f)
            list_ = {}
            list_2 = []
            for row in csv_reader:
                for l_key, l_value in dict(row).items():
                    list_[l_key] = l_value
                list_2.append(cls.create(**list_))
            return list_2
