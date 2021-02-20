#!/usr/bin/python3
"""doc"""


def read_lines(filename="", nb_lines=0):
    """doc"""
    line = ""
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            en_file = f.read()
            print(en_file, end="")
            return
        while nb_lines:
            line = f.readline()
            print(line, end="")
            nb_lines -= 1
