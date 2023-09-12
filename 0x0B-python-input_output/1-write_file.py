#!/usr/bin/python3
"""This module writes a string to a file and return the number of characters"""


def write_file(filename="", text=""):
    """Function that returns number of written character"""

    with open(filename, 'w', encoding="utf-8") as wd_f:
        nb_c = wd_f.write(text)
        return nb_c
