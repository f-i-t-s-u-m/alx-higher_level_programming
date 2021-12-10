#!/usr/bin/python3
''' OOP python '''


class Square():
    ''' Square that defines a square '''
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not(isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not(len(position) == 2) or not(all(isinstance(n, int) for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        print("position")
        return self.__position
    

    @position.setter
    def position(self, value):
        print(self.__position)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print("", end=" ")
                for _ in range(self.__size):
                    print("#", end="")
                print("")
