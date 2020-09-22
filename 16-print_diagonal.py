#!/usr/bin/python3
def print_diagonal(n):
        for i in range(n):
                for j in range(n + 1):
                        if j == i:
                                if n == 0:
                                        print()
                                else:
                                        print("{}\\".format((i)* " "))
