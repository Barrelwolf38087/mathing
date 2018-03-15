#!/usr/bin/python3
#Experimenting with new import statements to save a bit of memory
from sys import argv
from math import gcd
from common import validateInteger

def getGcf(*args):
    thisGcf = gcd(args[0], args[1])
    for i in args[2:]:
        thisGcf = gcd(thisGcf, i)
    print(thisGcf)
    

if __name__ == "__main__":
    print(str(getGcf(validateInteger(argv))))