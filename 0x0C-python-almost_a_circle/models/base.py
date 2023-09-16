#!/usr/bin/python3
""" This module is work with base class"""


class Base:
    """ First base class
    This class will be the "base" of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Method which initialize the attributes"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
