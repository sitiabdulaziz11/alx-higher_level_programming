#!/usr/bin/python3
"""This module works on inheritace"""

class MyList(list):
    """This class inherit from list"""

    def print_sorted(self):
        """ method that prints list in sorted
         (ascending) order."""

        if issubclass(MyList, list):
            sl = sorted(self)
            print(sl)
