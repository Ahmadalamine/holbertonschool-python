#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename) as f:
        f.read()
        for line in f:
            print(line, end='')

