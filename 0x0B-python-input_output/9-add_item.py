#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
try:
        mylist = load_from_json_file("add_item.json")
except:
        mylist = []
mylist += argv[1:]
save_to_json_file(mylist, "add_item.json")
