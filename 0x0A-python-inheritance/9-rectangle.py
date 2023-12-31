#!/usr/bin/python3
""" My Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """my Rectangle class
    class that inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        self.integer_validator("widith", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
            return self.__width * self.__height

    def __str__(self):
            return '[Rectangle] ' + str(self.__width) + '/' + str(
                    self.__height)
