#!/usr/bin/python3
"""This module returns list of a variable attribute and
    method of an object."""


def lookup(obj):
    """function that returns variable and object"""
    val = dir(obj)
    return val
