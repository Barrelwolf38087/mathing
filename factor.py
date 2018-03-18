#!/usr/bin/python3
import sys
import common

factorList = []
input = 0


def printResult():
    for thisFactor in factorList:
        print(thisFactor)

def doFactoring():
    numberToTry = 1
    while numberToTry <= input:
        if input % numberToTry == 0:
            factorList.append(numberToTry)
        numberToTry += 1


def getFactors(numberToFactor):
    numberToFactor = common.validateInteger(numberToFactor)
    factorList = []
    numberToTry = 1
    while numberToTry <= numberToFactor:
        if numberToFactor % numberToTry == 0:
            factorList.append(numberToTry)
        numberToTry += 1
    return factorList


#Main program logic
if __name__ == "__main__":
    try:
        input = common.validateInteger(sys.argv[1])
    except IndexError:
        print("Usage: factor.py number")
        exit(1)

    doFactoring()
    printResult()
    factorList = []
    input = 0