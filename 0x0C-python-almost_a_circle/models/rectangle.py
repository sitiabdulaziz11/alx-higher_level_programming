#!/usr/bin/python3
"""This module write class that inherit from previous Base class"""

from .base import Base


class Rectangle(Base):
    """My Rectangle class that inherits from previous Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError(" x must be an integer")

        if x <= 0:
            raise ValueError("x must be > 0")
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """ calculate and return the area of the Rectangle.
        """
        return self.__height * self.__width
    def display(self):
        """print representation of the Rectangle using '#' character
        accounting for 'x' and 'y'
        """
        for t in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
