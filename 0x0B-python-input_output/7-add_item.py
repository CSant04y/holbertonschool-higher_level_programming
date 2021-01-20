#!/usr/bin/python3
"""script to add all arguments to a Python list and save to a file"""


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_str = load_from_json_file("add_item.json")
except:
    json_str = []

json_str += argv[1:]

save_to_json_file(json_str, "add_item.json")
