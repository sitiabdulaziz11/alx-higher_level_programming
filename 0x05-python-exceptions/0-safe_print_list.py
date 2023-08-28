#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for t in my_list:
            if count < x:
                print('{}'.format(t), end="")
                count += 1
        print()
        return count
    except IndexError:
        print('out of index')
