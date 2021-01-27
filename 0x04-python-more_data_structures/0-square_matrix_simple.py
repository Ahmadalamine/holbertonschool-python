#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        new = matrix.copy()
        for i in range(len(matrix)):
            for j in i:
                new[i][j] = matrix[i][j] ** 2
        return new
