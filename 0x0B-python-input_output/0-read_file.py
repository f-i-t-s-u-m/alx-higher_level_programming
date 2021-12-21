#!/usr/bin/python3
''' python io file '''


def read_file(filename=""):
    ''' python class to read file '''

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
