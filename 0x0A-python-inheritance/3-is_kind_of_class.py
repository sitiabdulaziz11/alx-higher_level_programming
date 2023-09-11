#!/usr/bin/python3
"""This module check instance of the class"""


def is_kind_of_class(obj, a_class):
    """ check obj is instanc of a class
    or instance of inherited class"""

    if (isinstance(obj, a_class)):
        return True
    return False
