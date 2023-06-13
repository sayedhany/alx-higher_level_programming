#!/usr/bin/python3
""" append text to file"""


def append_write(filename="", text=""):
    """ function to append text"""
    with open(filename, mode="a", encoding="utf-8") as file1:
        num = file1.write(text)
        return num
