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
        print(sorted(self))
