#!/usr/bin/python3
"""this module contains one class"""


class Square:
    """this classs contains the constructor and on private attribute."""


    def __init__(self, size=0):
        """this functions is the const."""    


        try:
            __size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
