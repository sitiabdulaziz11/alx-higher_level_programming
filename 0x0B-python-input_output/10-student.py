#!/usr/bin/python3
"""
Module that defines My Student class
"""


class Student:
    """
    class that defines student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Function that initialize the attributes
        """

        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """retrievs student instance"""

        if isinstance(attrs, list) and all(
                isinstance(val, str) for val in attrs):
            res = {}
            for val in attrs:
                res[val] = getattr(self, val)
            return res
        return self.__dict__
