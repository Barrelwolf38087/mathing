#!/usr/bin/python3
from sys import argv


def checkAll():
    pass

def checkCommon():
    pass

def checkFactor():
    pass

def checkFactorPairs():
    pass

def checkGcf():
    pass

def checkPerfect():
    pass

def checkRoot():
    pass

modList = {
    'all': checkAll,
    'common': checkCommon,
    'factor': checkFactor,
    'factorpairs': checkFactorPairs,
    'gcf': checkGcf,
    'perfect': checkPerfect,
    'root': checkRoot
}

if __name__ == "__main__":
    try:
        input = argv[1:]
    except IndexError:
        print("Usage: test.py module|all [module 2...]")
    
    toCheck = list(filter(lambda x: True if x in modList else False, input))
    mismatch = list(filter(lambda x: False if x in modList else True, input))

    if len(mismatch) > 0: 
        print("Inputs did not match any modules:", ', '.join(list((str(i) for i in mismatch))))
