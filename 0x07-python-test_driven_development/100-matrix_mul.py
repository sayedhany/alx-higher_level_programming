#!/usr/bin/python3
"""
calculate the product of two matries
"""


def matrix_mul(m_a, m_b):
    """
    product function
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise ValueError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise ValueError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # perform matix multiplication
    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        res.append(row)
    return res
