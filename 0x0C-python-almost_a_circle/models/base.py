#!/usr/bin/python3
''' almost circule '''


class Base:
    ''' class of base '''
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None:
            self.__id = value
        else:
            self.__id = self.__nb_objects
