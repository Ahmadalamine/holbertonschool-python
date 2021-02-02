#!/usr/bin/python3
"""this module contains one class."""


class Square:
    """this class contains the constructor and on private attribute."""

    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        a = self.__size ** 2
        return a
