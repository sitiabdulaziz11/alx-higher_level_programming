#!/usr/bin/python3
""" Module that
write class MyInt that inherits from intass MyInt(int)
"""


def __eq__(self, other):
    """function that Override the equality operator"""

    return super().__ne__(other)


def __ne__(self, other):
    """function that Override the inequality operator"""

    return super().__eq__(other)
