#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        newm = map(lambda x: x * x, matrix)
        m=list(newm)
        return m
