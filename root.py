#!/usr/bin/python3
import sys
import common

def getRoot(root, radicand):
    if radicand >= 0:
        return radicand ** (1. / common.validateFloat(root))
    return -(-radicand) ** (1. / common.validateFloat(root))


if __name__ == "__main__":
    try:
        root = common.validateInteger(sys.argv[1])
        radicand = common.validateInteger(sys.argv[2])
        
        print(getRoot(root, radicand))
    except IndexError:
        print("Usage: root.py root radicand")