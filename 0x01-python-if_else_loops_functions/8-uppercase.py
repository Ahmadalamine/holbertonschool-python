#!/usr/bin/python3
def uppercase(str):
    res = []
    for i in str:
        if 96 < ord(i) < 123:
            i = ord(i) - 32
        res += str(i)
    print("{}".format(res))
