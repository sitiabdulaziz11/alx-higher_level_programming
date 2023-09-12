#!/usr/bin/python3
""" Module that creates object from ajsonfile"""

import json


def load_from_json_file(filename):
    """ Function that creates object from a "JSON file" """

    with open(filename, 'r') as fl:
        obj = json.load(fl)
    return obj
