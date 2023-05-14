#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for max1 in matrix:
        if len(matrix) == 0:
            print()
        for n in range(len(max1)):
            print('{:d}'.format(max1[n]),
                  end='\n' if n == len(max1) - 1 else ' ')
