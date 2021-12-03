#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key, 'none') != 'none':
        a_dictionary.pop(key)
    return a_dictionary
