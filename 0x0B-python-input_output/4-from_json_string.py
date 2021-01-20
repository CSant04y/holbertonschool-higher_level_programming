#!/usr/bin/python3
"""[function that returns an object (Python data structure)
    represented by a JSON string]
"""


import json


def from_json_string(my_str):
    """[Returns object from JSON]

    Args:
        my_str ([String]): [The string to be deserilized]
    """
    return json.loads(my_str)
