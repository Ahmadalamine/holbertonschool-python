#!/usr/bin/python3
def uppercase(str):
    res = []
    for i in str:
        if 96 < ord(i) < 121:
            i = ord(i) - 32
        res.append(i)
    l = join(res)
    print("{}".format(l))
