#!/usr/bin/python3
"""
print sorted
"""


class MyList(list):
    """class"""
    pass

    def print_sorted(self):
        """
        method
        """
        sorted_lisst = sorted(list(self))
        print(sorted_lisst)
