#!/usr/bin/python3
"""this module contains one class"""


class Square:
    """this classs contains the constructor and on private attribute."""
    def __init__(self, size=0):
        __size = size
        if type(self.__size) != int:
            raise("size must be an integer")
        if self.__size < 0
            raise("size must be >= 0")
