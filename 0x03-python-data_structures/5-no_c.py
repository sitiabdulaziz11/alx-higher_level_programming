#!/usr/bin/python3
def no_c(my_string):
    ns = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            ns += i
    return ns
