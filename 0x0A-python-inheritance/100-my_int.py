#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """Overides and inverts"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts"""
        return int(self) == int(other)
