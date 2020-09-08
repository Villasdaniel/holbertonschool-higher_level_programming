#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if idx >= 0 and idx < len(my_list):
                a = my_list.copy()
                a[idx] = element
                return a
        else:
                return my_list
