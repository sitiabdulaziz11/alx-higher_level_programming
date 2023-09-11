#!/usr/bin/python3
"""This module check instance of the class"""


def inherits_from(obj, a_class):
    """ function that check for instance"""

    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
                return True
    return False
