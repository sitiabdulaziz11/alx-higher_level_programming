#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        added_tuple_a = tuple_a + (0, 0)   # * (2 - len(tuple_a))
    else:
        added_tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        added_tuple_b = tuple_b + (0, 0)  # * (2 - len(tuple_b))
    else:
        added_tuple_b = tuple_b[:2]

    add1 = added_tuple_a[0] + added_tuple_b[0]
    add2 = added_tuple_a[1] + added_tuple_b[1]
    result = (add1, add2)
    return result
