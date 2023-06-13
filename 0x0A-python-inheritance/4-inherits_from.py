#!/usr/bin/python3
"""
is subclass
"""


def inherits_from(obj, a_class):
    """
    function to do it
    """
    return isinstance(obj, a_class) and type(obj) != a_class
