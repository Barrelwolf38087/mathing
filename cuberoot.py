#!/usr/bin/python3
import sys
import getfactors
import common

def getCubeRoot(num):
    if num >= 0:
        return num ** (1. / 3.)
    return -(-num) ** (1. / 3.)


if __name__ == "__main__":
    print(str(common.validateInteger(sys.argv[1])))
