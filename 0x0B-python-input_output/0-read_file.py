#!/usr/bin/python3
"""This module is reads a text file"""


def read_file(filename=""):
    with open("my_file_0.txt", 'r') as rd_f:
        for ln in rd_f:
            print(ln, end="")
