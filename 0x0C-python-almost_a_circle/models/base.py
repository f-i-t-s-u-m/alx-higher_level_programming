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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []
