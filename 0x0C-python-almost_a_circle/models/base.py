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
        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file class methpd"""
        newlist = list()
        for objs in list_objs:
            newlist.append(objs.to_dictionary())
        with open(cls.__name__+'.json', "w") as jsfile:
            json.dump(json.loads(cls.to_json_string(newlist)), jsfile)
