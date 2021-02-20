#!/usr/bin/python3
"""doc"""


def read_lines(filename="", nb_lines=0):
    """doc"""
    line = ""
    with open(filename) as f:
        while nb_lines:
            line = f.readline()
            print(line, end="")
            nb_lines -= 1
