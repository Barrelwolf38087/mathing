#!/usr/bin/python3
from sys import argv
from common import validateInteger
from common import convertibleToInteger
from math import gcd

numbers = []
for i in argv:
    if convertibleToInteger(i):
        numbers.append(validateInteger(i))


def getGcf(*args):
    return gcd()


###OLD, CRAPPY CODE BELOW###


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