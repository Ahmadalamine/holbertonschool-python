#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for i in range(len(matrix)):
        for j in range(len(i)):
            print("{:d}".format(matrix[i][j]), end=' ')
        print
