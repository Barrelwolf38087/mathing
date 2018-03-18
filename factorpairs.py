#!/usr/bin/python3

#To be merged into factor.py

from sys import argv
from common import validateInteger
from factor import getFactors
from root import getRoot


def getFactorPairs(input):
    num = validateInteger(input)
    factors = getFactors(num)

    if len(factors) % 2 != 0:
        factors.insert(factors.index(getRoot(2, num)), int(getRoot(2, num)))

    h = int(len(factors) / 2)

    a = factors[:h]
    b = factors[h:]
    b.reverse()

    return list(map(lambda x: (a[x], b[x]), range(0, len(a))))


if __name__ == "__main__":
    for i in getFactorPairs(argv[1]):
        print(i)