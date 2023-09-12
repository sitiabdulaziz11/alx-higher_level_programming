#!/usr/bin/python3
"""Module that writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """Function writes an object to a text file using a json representation"""

    with open(filename, 'w') as fl:
        json.dump(my_obj, fl)
