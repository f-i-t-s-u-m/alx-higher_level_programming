#!/usr/bin/python3
''' python file '''


def write_file(filename="", text=""):
    ''' write to file'''

    size = 0
    with open(filename, "w", encoding="UTF-8") as f:
        print(text, file=f, end="")
    return len(text)
