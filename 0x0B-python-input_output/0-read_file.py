#!/usr/bin/python3
''' python io file '''


def read_file(filename=""):
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
