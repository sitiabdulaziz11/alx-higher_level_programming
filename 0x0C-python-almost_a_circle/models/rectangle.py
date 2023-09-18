#!/usr/bin/python3
"""
This module write class that inherit from previous Base class
"""

from .base import Base


class Rectangle(Base):
    """My Rectangle class that inherits from previous Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance or attributes of the class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter function for __width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter function for __width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """
        getter function for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        getter function for x.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        setter function for x.
        """
        if not isinstance(val, int):
            raise TypeError(" x must be an integer")

        if val < 0:
            raise ValueError("x must be > 0")
        self.__x = val

    @property
    def y(self):
        """
        getter function for y.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        setter function for y.
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be > 0")
        self.__y = val

    def area(self):
        """ calculate and return the area of the Rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """print representation of the Rectangle using '#' character
        accounting for 'x' and 'y'
        """
        for t in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns a string format of the rectanglei with '#' character
        """
        return (
                f"[{type(self).__name__}] ({self.id})"
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """
        assign key/value argument to attributes
        kwargs is skipped if args is not empty
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of a Rectangle
        """
        rec_dict = {'y': self.y,
                    'x': self.x,
                    'id': self.id,
                    'width': self.width,
                    'height': self.height
                    }
        return rec_dict
