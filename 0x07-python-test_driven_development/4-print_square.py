#!/usr/bin/python3
"""
print square
"""


def print_square(size):
    """
    print square of #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
