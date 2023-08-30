#!/usr/bin/python3
"""This is first time of oblect oriented programming in python"""


class Square:

    """This is  square class that defines square"""
    def __init__(self, size=0):
        """This is constructor method"""
        self.__size = size

    def func(size):
        """This is first methode in python class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("value must be >= 0")


squ1 = Square(5)
aqu2 = Square(2)
