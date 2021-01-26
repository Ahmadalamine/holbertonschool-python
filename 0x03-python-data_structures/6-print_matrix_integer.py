#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for items in matrix:
        for item in items:
            print("{:d}".format(matrix[i][j]), end=' ')
        print
