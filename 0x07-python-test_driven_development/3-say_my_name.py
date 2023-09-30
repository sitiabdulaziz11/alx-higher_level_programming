#!/usr/bin/python3
"""
This module prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This method prints first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My name is {:s}".format(first_name))
