#!/usr/bin/python3
"""This module is Square class that inherits from Rectangle class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the instance of the class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter function that returns size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        settre function for size
        """
        self.width = size
        self.height = size

    def __str__(self):
        return (
                f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}"
                )

    def update(self, *args, **kwargs):
        """
        Method that  update the Square class by adding
        a public method named update
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Function that update class Square by adding the public method
         that returns the dictionary representation of a Square
         """
        sqr_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return sqr_dict
