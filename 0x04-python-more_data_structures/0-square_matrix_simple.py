#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newmatrix[i][j] = matrix[i][j] * matrix[i][j]
    return newmatrix


dm = square_matrix_simple([[1,2,3],[4,5,6],[7,8,9]])
print(dm)
