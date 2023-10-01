#!/usr/bin/python3
"""
module that prints square with the character #
"""


def print_square(size):
    """
    This Function print square with # sign.
    """
    if not isinstance(size, int) or size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
