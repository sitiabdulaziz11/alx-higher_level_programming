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

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrievs student instance"""
        return self.__dict__
