#!/usr/bin/python3

#This one needs serious debugging!

import sys
import common
import getfactors

factors = getfactors.getFactors(common.validateInteger(sys.argv[1]))

if len(factors) % 2 != 0:
    halfLen = int((len(factors) - 1) / 2)
    squareroot = factors[halfLen]
else:
    halfLen = int(len(factors) / 2)

try:
    factors.insert(factors.index(squareroot), squareroot)
except NameError:
    pass

setA = []
setB = []

for i in range(0, halfLen - 1):
    setA.append(factors[i])
for i in range (1, halfLen):
    setB.append(factors[-i])


def getFactorPairs(num):
    factors = getfactors.getFactors(common.validateInteger(sys.argv[1]))
    pairs = []

    if len(factors) % 2 != 0:
        halfLen = int((len(factors) - 1) / 2)
        squareroot = factors[halfLen]
    else:
        halfLen = int(len(factors) / 2)

    try:
        factors.insert(factors.index(squareroot), squareroot)
    except NameError:
        pass

    setA = []
    setB = []

    for i in range(0, halfLen - 1):
        setA.append(factors[i])
    for i in range (1, halfLen):
        setB.append(factors[-i])

    for i in range(0, len(setA) - 1):
        pairs[i] = [setA[i], setB[i]]

    return pairs


if __name__ == "__main__":
    for i in range(len(setA)):
        print(str(setA[i]) + " x " + str(setB[i]))

# firstFactors = []
# secondFactors = []

# input = common.validateInteger(sys.argv[1])
# factors = getfactors.getFactors(input)

# def getFactorPairs(num):
#     input = common.validateInteger(num)
#     factors = getfactors.getFactors(input)
#     firstFactors = []
#     secondFactors = []
#     for thisIndex in range(0, int(len(factors) / 2 - 1)):
#         firstFactors.append(factors[thisIndex])
#     for thisIndex in range(int(len(factors) / 2), len(factors) - 1):
#         secondFactors.append(factors[thisIndex])
#     secondFactors.reverse()
    
#     return dict(zip(firstFactors, secondFactors))


# for thisIndex in range(0, int(len(factors) / 2 - 1)):
#     firstFactors.append(factors[thisIndex])

# for thisIndex in range(int(len(factors) / 2), len(factors) - 1):
#     secondFactors.append(factors[thisIndex])

# secondFactors.reverse()

# #for thisIndex in range(0, len(firstFactors) - 1):
# #    factorPairs[firstFactors[thisIndex]] += secondFactors[thisIndex]

# if __name__ == "__main__":
#     for thisIndex in range(0, len(firstFactors) - 1):
#         print(str(firstFactors[thisIndex]) + " x " + str(secondFactors[thisIndex]))