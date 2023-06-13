#!/usr/bin/python3
"""
Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rect
    """
    def __init__(self, width, height):
        super().integer_validator(width, height)
        self.__width = width
        self.__height = height
