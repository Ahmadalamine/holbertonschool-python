#!/usr/bin/python3
"""this module contains one class."""


class Square:
    """this class contains the constructor and on private attribute."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in position:
                    if not isinstance(i, int) or i < 0:
                        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                    if not isinstance(i, int) or i < 0:
                        raise TypeError("position must be a tuple of 2 positive integers")
        y = list(self.position)
        y[0] = value[0]
        y[1] = value[1]
        self.__position = tuple(value)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for z in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def area(self):
        return self.__size ** 2
