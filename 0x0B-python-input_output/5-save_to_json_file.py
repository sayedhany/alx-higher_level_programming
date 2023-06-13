#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function to Save Object to a file """
    with open(filename, mode="w", encoding="utf-8") as file1:
        json.dump(my_obj, file1)
