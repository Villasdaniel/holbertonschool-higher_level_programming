#!/usr/bin/python3
def rotate_left_list(my_list=[], number_rotation=0):
        i = number_rotation
        n_list = my_list.copy()
        n_list = []
        for i, j in (enumerate(my_list)):
                i = i + 1
                n_list[j] = my_list[i]
        return n_list
