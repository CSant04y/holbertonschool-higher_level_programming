#!/usr/bin/python3
"""defines function to write JSON representatin of an object to file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes json representation in file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
