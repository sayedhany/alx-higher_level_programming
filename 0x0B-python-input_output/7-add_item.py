#!/usr/bin/python3
"""Create object from a JSON file"""
from sys import argv
import json
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
new_data = []
if os.path.exists("add_item.json"):
    new_data = list(load_from_json_file("add_item.json"))
for arg in argv[1:]:
    new_data.append(arg)
save_to_json_file(new_data, "add_item.json")
