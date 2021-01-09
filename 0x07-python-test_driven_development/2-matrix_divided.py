#!/usr/bin/python3
"""This function takes a list and divideds each element of list"""


def matrix_divided(matrix, div):
    """The function takes in matrix and divideds elements by two dec"""
    error_mssg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_mssg)
    num_row = 0
    row_len = []
    new_matrix = []
    for i in matrix:
        if type(i) is not list:
            raise TypeError(error_mssg)
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(error_mssg)

    row_len = len(matrix[0])
    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num/div, 2) for num in list] for list in matrix]
