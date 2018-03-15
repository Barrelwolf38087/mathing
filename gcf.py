#!/usr/bin/python3
#Experimenting with new import statements to save a bit of memory
from sys import argv
from math import gcd
from factor import getFactors
from common import validateIntegers



numbers = validateIntegers(argv)

def getGcf(*args):
    fll = list(map(getFactors, args))
    a = []
    for i in fll:
        pass


if __name__ == "__main__":
    print(str(getGcf(*numbers)))


###WARNING:Old, crummy code below###


# import factor

# numbers = []

# for i in sys.argv:
#     if i != __name__ and common.convertibleToInteger(i):
#         numbers.append(common.validateInteger(i))


# #il should be a list of lists
# def allContain(il, value):
    
#     for thisList in il:
#         if not list.__contains__(thisList, value):
#             return False

#     return True

# def getGcf(numbers): #reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
#     factorListList = []
#     possible = []
#     #commonFactors = []
#     #tryThis = 1

#     for i in numbers:
#         factorListList.append(factor.getFactors(i))


#     # while tryThis <= max(numbers):
#     #     if allContain(factorListList, tryThis):
#     #         commonFactors.append(tryThis)
    
#     # return max(commonFactors)


# if __name__ == "__main__":
#     print(str(getGcf(numbers)))