#!/usr/bin/python3
#Experimenting with new import statements to save a bit of memory
from sys import argv
from common import validateInteger
from common import convertibleToInteger
from math import gcd

numbers = []

#Beware the unnecessarily long line
numbers = list(map(lambda x: validateInteger(x) if convertibleToInteger(x) else None, argv))

#I take no credit for math.gcd()
def getGcf(*args):
    return gcd(*args)

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