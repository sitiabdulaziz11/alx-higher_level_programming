#!/usr/bin/python3
""" This module checke objects in the class"""


def is_same_class(obj, a_class):
    """ return true
    if the object is exactly an instance of the specified class
    return false otherwise"""

    if type(obj) is a_class:
        return True
    return False
