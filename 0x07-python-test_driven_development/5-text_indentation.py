#!/usr/bin/python3
"""
This module print a text with 2 new lines after each of these characters
'.', "?", ':'
"""


def text_indentation(text):
    """
    This method print text with 2 new lines the above characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delm in ".?:":
        text = (delm + "\n\n").join(
                [line.strip(" ") for line in text.split(delm)])
        print(text, end="")
