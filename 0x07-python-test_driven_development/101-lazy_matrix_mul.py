#!/usr/bin/python3
"""Module lazy_matrix_mul
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
        """Multiplies m_a and m_b using
        matmuly.
        """
        return numpy.dot(m_a, m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
