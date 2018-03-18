#!/usr/bin/python3
from sys import argv
from common import validateInteger
from common import validateFloat

def getRoot(root, radicand, perfect=False):
    if radicand >= 0:
        result = radicand ** (1. / validateFloat(root))
    else:
        result = -(-radicand) ** (1. / validateFloat(root))

    if perfect:
        return round(result)
    else:
        return result

if __name__ == "__main__":
    try:
        root = validateInteger(argv[1])
        radicand = validateInteger(argv[2])

    except IndexError:
        print("Usage: root.py root radicand [perfect]")

    try:
        perfect = True if argv[3].lower() == "perfect" else False
    except IndexError:
        perfect = False

    print(str(getRoot(root, radicand, perfect)))

