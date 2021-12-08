#!/usr/bin/python3
''' file defines a square '''


class Square():
    ''' class that define square '''
    def __init__(self, size=0):
        if type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is int:
            self._Square__size = size
        else:
            raise TypeError("size must be an integer")
