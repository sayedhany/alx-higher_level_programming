#!/usr/bin/python3
"""
write text to file
"""


def write_file(filename="", text=""):
    """function to do it"""
    with open(filename, mode="w", encoding="utf-8") as file1:
        sum_of_chars = file1.write(text)
        return sum_of_chars
