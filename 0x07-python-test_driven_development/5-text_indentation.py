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
        ln = text.split(delm)
        form_ln = [ln.strip() for ln in ln]
        form_text = (delm + "\n\n").join(form_ln)
        text = form_text
    print(text, end="")
