#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda num: list(map(lambda j: j * j, i)), matrix))