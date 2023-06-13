#!/usr/bin/python3
"""
print sorted
"""


class MyList(list):
    """MyClass inherit from list"""
    pass

    def print_sorted(self):
        """
        print sorted list
        """
        sorted_lisst = sorted(list(self))
        print(sorted_lisst)
