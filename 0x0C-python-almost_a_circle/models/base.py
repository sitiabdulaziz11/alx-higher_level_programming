#!/usr/bin/python3
""" This module is work with base class"""

import json


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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that writes the json string representation to a file
        """
        f_name = f"{cls.__name__}.json"

        json_val = cls.to_json_string(list_objs)

        with open(f_name, 'w') as fil:
            fil.write(json_val)
    
    @staticmethod
    def from_json_string(json_string):
        """
        Function that returns the list of the Json string representation 
        """
        if json_string is None or json_string == "":
            return "[]"
        else:
            data = json.loads(json_string)
            if isinstance(data, list) and all(isinstance(
                item, dict) for item in data):
                return data
    @classmethod
    def create(cls, **dictionary):
        """
        Function that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        if args:
            attr_name = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_name[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def load_from_file(cls):
        """Construct the filename based on the class name
        """
        f_name = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []
        else:
            with open(f_name, 'r') as fi:
                data = json.load(fi)
                instances = []

                for item in data:
                    instance = cls.from_json_string(item)
                    instances.append(instance)

                return instances
