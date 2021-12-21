#!/usr/bin/python3
''' python file '''


def append_write(filename="", text=""):
    ''' write to file'''

    size = 0
    with open(filename, "a", encoding="UTF-8") as f:
        print(text, file=f, end="")
    return len(text)
