#!/usr/bin/python3
"""This module is to add two integers
or two floats
after casting.

"""


def add_integer(a, b=98):
    """ Function that adds two integers.
    @a: first value  @b: second value.
    return a + b."""

    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        b = int(b)
    return a + b
