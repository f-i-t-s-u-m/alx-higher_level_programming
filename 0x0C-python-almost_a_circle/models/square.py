#!/usr/bin/python3
""" python square file """

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        "return size"
        return self.width

    @size.setter
    def size(self, value):
        """ size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update area"""

        if len(args) == 0:
            for k, v in kwargs.items():
                exec(f"self.{k} = {v}")
        else:
            self.id = args[0]
            for i, val in enumerate(args[1:]):
                if i == 0:
                    self.size = val
                elif i == 1:
                    self.x = val
                elif i == 2:
                    self.y = val

    def to_dictionary(self):
        """ square to dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """ return square string """
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height))
