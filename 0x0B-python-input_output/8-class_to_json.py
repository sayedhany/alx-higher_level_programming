#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    new_dict = {}

    for attr in dir(obj):
        attr_value = getattr(obj, attr)

        if isinstance(attr_value, (list, dict, str, int, bool)):
            new_dict[attr] = attr_value
    return new_dict
