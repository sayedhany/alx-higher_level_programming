#!/usr/bin/python3
"""
divide matix by div
"""


def matrix_divided(matrix, div):
    """
    divide matix with div
    """
    def is_list_of_lists(variable):
        """
        check if matrix is list of lists
        """
        bool_list = isinstance(variable, list)
        bool_lists = all(isinstance(item, list) for item in variable)
        return bool_list and bool_lists
    mess_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not is_list_of_lists(matrix):
        raise TypeError(mess_err)
    len_row = len(matrix[0])
    for row in matrix:
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [
            [round(elem / div, 2) for elem in row]
            for row in matrix
            ]
    return divided_matrix
