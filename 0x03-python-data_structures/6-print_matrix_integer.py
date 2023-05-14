#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for max1 in matrix:
        for element in max1:
            print("{:d} ".format(element), end="")
        print()
