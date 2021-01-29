#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print(my_list[i], end="")
    except IndexError:
            print("{:d} is out of bound".format(x))
    return i

