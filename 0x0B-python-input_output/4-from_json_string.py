#!/usr/bin/python3
"""Module that return object represented by josn string"""

import json


def from_json_string(my_str):
    """Function that return object of json"""

    ob_py = json.loads(my_str)
    return ob_py
