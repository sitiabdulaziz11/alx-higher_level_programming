#!/usr/bin/python3
"""Module that append string at the end of a text file"""


def append_write(filename="", text=""):
    """Function append string and return
    number of added characters"""

    with open(filename, 'a', encoding="utf-8") as ap:
        appnd = ap.write(text)
        return appnd
