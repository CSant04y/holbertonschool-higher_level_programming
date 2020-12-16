#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for len1 in range(len(matrix)):
        for len2 in range(len(matrix[len1])):
            if len2 == len(matrix[len1]) - 1:
                print("{:d}".format(matrix[len1][len2]), end="")
            else:
                print("{:d}".format(matrix[len1][len2]), end=" ")
        print()
