#!/usr/bin/python3
""" Module that inserts aline of text to afile"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string.
    """

    with open(filename) as ap:
        fil = ""
        for ln in ap:
            fil += ln
            if search_string in ln:
                fil += new_string
    with open(filename, 'w') as wr:
        wr.write(fil)
