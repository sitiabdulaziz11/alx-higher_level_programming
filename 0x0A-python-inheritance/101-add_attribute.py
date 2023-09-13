#!/usr/bin/python3
"""
Write a function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible, or raise TypeError."""

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add a new attribute")
