#!/usr/bin/python3
""" My Rectangle module"""

BaseGeometry = __import__('7-base_geometry').baseGeometry


class Rectangle:
    """my Rectangle class
    that inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        self.integer_validator("widith", width)
        self.integer_validator("height", height)

        self.__width = width
        self.height = height
