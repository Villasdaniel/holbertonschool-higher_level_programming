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
        for i in range(len(matrix)):
                a = []
                if (len(matrix[0]) != len(matrix[i])):
                        raise TypeError("Each row of the matrix\
 must have the same size")
                for j in range(len(matrix[i])):
                        if type(j) not in [int, float]:
                                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
                        a.append(round(((matrix[i][j]) / div), 2))
                b.append(a)
        return b
