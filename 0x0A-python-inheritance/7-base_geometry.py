#!/usr/bin/python3
"""This module check instance of the class"""


class BaseGeometry:
    """ empty class"""

    def integer_validator(self, name, value):
        """ My public instance method"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """function only with exceptions"""
        raise Exception("area() is not implemented")
