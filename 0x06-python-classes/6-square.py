#!/usr/bin/python3
''' OOP python '''


class Square():
    ''' Square that defines a square '''
    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    def area(self):
        '''method that return area of the square'''
        return self.__size * self.__size

    @property
    def size(self):
        ''' method that return the size of square'''
        return self.__size

    @property
    def position(self):
        ''' method to return position'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' method to set psotition'''
        if not(isinstance(value, tuple)) and not(len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not(all(isinstance(n, int) for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        ''' method to set size'''
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        ''' method to print '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
