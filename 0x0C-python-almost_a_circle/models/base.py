#!/usr/bin/python3
''' almost circule '''

import json


class Base:
    ''' class of base '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to json string"""
        a = list()
        if list_dictionaries is None or list_dictionaries is []:
            return []
        for dics in list_dictionaries:
            a.append(dics)
        return json.dumps(a)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file class methpd"""
        with open(cls.__name__+'.json', "w") as jsfile:
            json.dump(cls.to_json_string(list_objs[0:].to_dictionary()), jsfile)
