#!/usr/bin/python3
"""doc"""


class BaseGeometry:
    """doc"""

    def area(self):
        """foc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """doc"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")