#!/usr/bin/python3
"""create square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """init method"""
        if isinstance(size, str):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
