#!/usr/bin/python3
"""This module defines rectangle class"""

class Rectangle:
    """A class that defines rectangr"""


    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.wdith = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._with = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self.width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
