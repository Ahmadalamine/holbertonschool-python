#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 96 < ord(i) < 121:
            i -= 32
        res = res + i
    print(res)
