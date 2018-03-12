#!/usr/bin/python3
import sys
import common

input = common.validateInteger(sys.argv[1])

for thisTry in range(0, abs(input) + 1):
    if thisTry ** 3 == abs(input):
        print("True")
        exit(0)

print("False")
exit(0)