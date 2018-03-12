#!/usr/bin/python3
import sys
import factor
import common

#il should be a list of lists
def allContain(il, value):
    true = True

    if type(il[0]) != "list":
        return None

    #list.__contains__()