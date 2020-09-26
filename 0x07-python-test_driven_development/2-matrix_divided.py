#!/usr/bin/python3
"""
Function that divide matrix elements


"""


def matrix_divided(matrix, div):
        """
        divide matrix elements
        """
        b = []
        if type(div) not in [int, float]:
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("Division by Zero")
        for i in matrix:
                a = []
                if type(i) is not list:
                        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
                if (len(matrix[0]) != len(i)):
                        raise TypeError("Each row of the matrix\
 must have the same size")
                for j in range(len(i)):
                        if (type(i[j]) is not int) and (type(i[j]) is not float):
                                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
                        a.append(round(((i[j]) / div), 2))        
                b.append(a)
        return b
