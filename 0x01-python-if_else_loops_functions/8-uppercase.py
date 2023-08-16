#!/usr/bin/python3
def uppercase(str):
    for i in str:
        k = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            k = k - 32
        print("{}".format(chr(k)), end="")
    print("\n")
