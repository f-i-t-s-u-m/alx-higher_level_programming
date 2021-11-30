#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        newMat = list()
        for m in matrix:
            newMat.append(list(map(lambda a: a ** 2, m)))
        return newMat
