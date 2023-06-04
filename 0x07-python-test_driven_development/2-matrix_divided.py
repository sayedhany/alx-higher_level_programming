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
        return isinstance(variable, list) and all(isinstance(item, list) for item in variable)
    if not is_list_of_lists(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_row = len(matrix[0])
    for row in matrix:
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    divided_matrix = list(map(lambda row: list(map(lambda x: round(x/div, 2), row)), matrix))
    return divided_matrix
