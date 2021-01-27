#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newmatrix[i][j] = matrix[i][j] * matrix[i][j]
    return newmatrix
