#!/usr/bin/python3
"""
Module inherit from other class
"""

Rectangle = __import__('9-rectangle').rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square:
    """
    my square class
    """
    def __init__(self, size):
        """Function that initialize attributs"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
