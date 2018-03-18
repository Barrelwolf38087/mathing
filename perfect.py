#!/usr/bin/python3
from sys import argv
from common import validateInteger

def checkPerfectPower(power, value):
    inputValue = validateInteger(value)
    inputPower = validateInteger(power)

    for i in range(abs(inputValue)):
        if i ** inputPower == abs(inputValue):
            return True
    return False

if __name__ == "__main__":
    try:
        print(str(checkPerfectPower(argv[1], argv[2])))
    except IndexError:
        print("Usage: perfect.py exponent number")