#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename) as f:
        data = f.read()
        print(data)
