#!/usr/bin/python3
"""Module that returns JSON representation of an object"""


import json


def to_json_string(my_obj):
    """Function that returns the json representation of an object"""

    js = json.dumps(my_obj)
    return js
