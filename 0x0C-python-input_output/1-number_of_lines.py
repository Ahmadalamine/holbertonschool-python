#!/usr/bin/python3
"""doc"""


def number_of_lines(filename=""):
    """doc"""
    nb_of_line = 0
    with open(filename, 'r') as f:
        f.readline()
        nb_of_line += 1
