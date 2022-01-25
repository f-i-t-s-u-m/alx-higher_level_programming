#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    ''' class of rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not(isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0 ")
        self.__x = value

    @y.setter
    def y(self, value):
        if not(isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0 ")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def update(self, *args):
        super().__init__(args[0])
        for i, val in enumerate(args[1:]):
            if i == 0:
                self.width = val
            elif i == 1:
                self.height = val
            elif i == 2:
                self.x = val
            elif i == 3:
                self.y = val

    def display(self):
        for _ in range(self.y):
            print(" ")
        for _ in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ return string """
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
