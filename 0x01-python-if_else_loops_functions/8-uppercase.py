#!/usr/bin/python3
def uppercase(str):
    res = list(str)
    for i in range(len(res)):
        if 96 < ord(str[i]) < 123:
            res[i] = ord(res[i]) - 32
            res[i] = chr(res[i])
    r = "".join(res)
    print("{}".format(r))

