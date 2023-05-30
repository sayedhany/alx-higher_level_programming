#!/usr/bin/python3
"""create square"""


class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """init method"""
        self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """return size value"""
        return self.__size

    @size.setter
    def size(self, size):
        """set size value"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return area of square"""
        return self.__size ** 2

    @property
    def position(self):
        """print position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print # * size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)   
