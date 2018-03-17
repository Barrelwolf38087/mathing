#!/usr/bin/python3

#To be merged into factor.py

from sys import argv
from common import validateInteger
from factor import getFactors


# def getFactorPairs(input):
#     factors = getFactors(validateInteger(input))

#     if len(factors) % 2 != 0:
#         halfLen = int((len(factors) - 1) / 2)
#         squareroot = factors[halfLen]
#         factors.insert(factors.index(squareroot), squareroot)
#     else:
#         halfLen = int(len(factors)) - 2

#     setA = [x for x in factors[:halfLen + 1]]
#     setB = [x for x in factors[halfLen + 1:]]
#     setB.reverse()
    
#     rv = []

#     for i in setA:
#         rv.append((i, setB[setA.index(i)]))
#     return rv
#     #return list(map(lambda x: (setA[x], setB[x]), range(0, len(setA))))


# if __name__ == "__main__":
#     for x in getFactorPairs(argv[1]):
#         print(x)