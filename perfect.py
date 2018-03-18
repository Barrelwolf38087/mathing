#!/usr/bin/python3
from sys import argv
from common import validateInteger

def checkPerfectPower(power, value, returnRoot=False):
    inputValue = validateInteger(value)
    inputPower = validateInteger(power)

    if returnRoot:
        from root import getRoot

    result = "False"

    for i in range(abs(inputValue)):
        if i ** inputPower == abs(inputValue):
            result = "True\n" + str(getRoot(inputPower, inputValue, True)) if returnRoot else "True"

    return result

if __name__ == "__main__":
    try:
        power = validateInteger(argv[1])
        base = validateInteger(argv[2])
    except IndexError:
        print("Usage: perfect.py exponent number [root]")
        exit()
    
    root = False

    try:
        if argv[3].lower() == "root":
            root = True
    except IndexError:
        pass

    print(checkPerfectPower(power, base, root))