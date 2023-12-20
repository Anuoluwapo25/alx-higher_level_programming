#!/usr/bin/python3

"""
Module: 2-matrix_divided
Method that divides all element in a list(matrix)
and returns a new list of matrix
"""


def matrix_divided(matrix, div):
    """
    divides elements of list(mattix)
    """
    new_mat = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(msg)
    elif len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(msg)
        if len(rows) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        new_list = []
        for cols in rows:
            if type(cols) not in [int, float]:
                raise TypeError(msg)
            if type(div) not in [int, float]:
                raise TypeError('div must be a number')
            new_list.append(round(cols/div, 2))
        new_mat.append(new_list)

    return new_mat
