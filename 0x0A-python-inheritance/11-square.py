#!/usr/bin/python3
"""
square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """init method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of a square"""
        return self.__size ** 2
    def __str__(self):
        """return a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
