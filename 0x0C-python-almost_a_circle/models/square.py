#!/usr/bin/python3
""" python square file """


from models.rectangle import Rectangle

class Square(Rectangle):
    """square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init square class"""
        super().__init__(size, size, x, y, id)
