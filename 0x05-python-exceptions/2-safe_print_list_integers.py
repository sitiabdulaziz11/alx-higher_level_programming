#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    l = 0
    try:
        for i in my_list:
            print('{:d}'.format(i), end="")
            l += 1
        print()
        return l
    except (TypeError, ValueError):
        return False 
