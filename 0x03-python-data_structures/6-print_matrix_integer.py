#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for mat in matrix:
            for n in mat:
                if n == mat[-1]:
                    print("{:d}".format(n), end='')
                else:
                    print("{:d}".format(n), end=' ')
            print()
