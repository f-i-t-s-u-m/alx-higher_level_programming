#!/usr/bin/python3
'''a suare that define square'''


class Square():
    ''' a class of suare'''
    def __init__(self, size=0):
        if type(size) is int:
            self.__size = size * size
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size
