#!/usr/bin/python3
"""module Technical preparation"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    trg = [[1]]
    while len(trg) != n:
        trg1 = trg[-1]
        tem_val = [1]

        for h in range(len(trg1) - 1):
            tem_val.append(trg1[h] + trg1[h + 1])
        tem_val.append(1)
        trg.append(tem_val)
    return trg
