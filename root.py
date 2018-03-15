#!/usr/bin/python3
from sys import argv
from common import validateInteger
from common import validateFloat

def getRoot(root, radicand):
    if radicand >= 0:
        return radicand ** (1. / validateFloat(root))
    return -(-radicand) ** (1. / validateFloat(root))


if __name__ == "__main__":
    try:
        root = validateInteger(argv[1])
        radicand = validateInteger(argv[2])
    
        print(str(getRoot(root, radicand)))

    except IndexError:
        print("Usage: root.py root radicand")