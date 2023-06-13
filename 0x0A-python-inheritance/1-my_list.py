#!/usr/bin/python3
"""
print sorted
"""


class MyList(list):
    """
    function to print sorted
    """
    def print_sorted(self):
        sorted_lisst = sorted(self)
        print(sorted_lisst)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
