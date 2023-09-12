#!/usr/bin/python3
"""This module is reads a text file"""


def read_file(filename="my_file_0.txt"):
    """ Function that read text and print to stdout"""

    with open(filename, 'r', encoding='utf-8') as rd_f:
        for ln in rd_f:
            print(ln, end="")
