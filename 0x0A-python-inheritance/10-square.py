#!/usr/bin/python3
"""
Module inherit from other class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """my square class
    Square class that inherits from Rectangle class
    """
    def __init__(self, size):
        """Function that initialize attributs"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
