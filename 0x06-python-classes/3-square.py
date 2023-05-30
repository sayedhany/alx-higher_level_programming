#!/usr/bin/python3
"""create square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """init method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return area of square"""
        return self.__size ** 2
