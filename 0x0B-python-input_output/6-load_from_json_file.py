#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """function to do it"""
    with open(filename, mode="r", encoding="utf-8") as file1:
        return json.load(file1)
