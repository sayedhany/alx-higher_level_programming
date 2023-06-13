#!/usr/bin/python3
"""
print test
"""


def read_file(filename=""):
    """ read text ang print it"""
    with open(filename, encoding="utf-8") as file1:
        print(file1.read(), end="")
