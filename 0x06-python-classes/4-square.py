#!/usr/bin/python3
''' square difines a square'''


class Square():
    ''' Square that define square '''
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int and value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        return self.__size
