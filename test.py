#!/usr/bin/python3
from sys import argv

def checkFunctionality(correct, function, *args):
    if function(*args) != correct: 
        return False
    return True


def checkCommon():
    print("Checking common...")
    errors = 0
    try:
        import common
    except ModuleNotFoundError:
        print("Module not found!")
        return
    
    if not hasattr(common, 'validateInteger'):
        print("Missing attribute validateInteger")
        errors += 1
    else:
        if not checkFunctionality(32, common.validateInteger, 32):
            print("validateInteger fails with normal int 32")
            errors += 1
        if not checkFunctionality(32, common.validateInteger, '32'):
            print("validateInteger fails with stringed int '32'")
            errors += 1
        if not checkFunctionality(32, common.validateInteger, 'abc3.def2ghi'):
            print("validateInteger fails with bad stringed int 'abc3.def2ghi'")
            errors += 1

    if not hasattr(common, 'validateIntegerToString'):
        print("Missing attribute validateIntegerToString")
        errors += 1
    else:
        if not checkFunctionality('32', common.validateIntegerToString, 32):
            print("validateIntegerToString fails with normal int 32")
            errors += 1
        if not checkFunctionality('32', common.validateIntegerToString, '32'):
            print("validateIntegerToString fails with stringed int '32'")
            errors += 1
        if not checkFunctionality('32', common.validateIntegerToString, 'abc3.def2ghi'):
            print("validateIntegerToString fails with bad stringed int 'abc3.def2ghi'")
            errors += 1

    # if not hasattr(common, 'validateIntegers'):
    #     print("Missing attribute validateIntegers")
    #     errors += 1
    # else:
    #     if not checkFunctionality([32, 64], common.validateIntegers, ['stuff', 32, 64])
    #         print("validateIntegers fails with ['stuff', 32, 64]")
    #         errors += 1
    #     if not checkFunctionality([32, 64], common.validateIntegers, [32, 64]):
    #         print("validateIntegers fails with [32, 64]")
    #         errors += 1

    if not hasattr(common, 'validateFloat'):
        print("Missing attribute validateFloat")
        errors += 1
    else:
        if not checkFunctionality(32.5, common.validateFloat, 32.5):
            print("validateFloat fails with normal float 32.5")
            errors += 1
        if not checkFunctionality(32.5, common.validateFloat, '32.5'):
            print("validateFloat fails with stringed float '32'")
            errors += 1
        if not checkFunctionality(32.5, common.validateFloat, 'abc3def2ghi.5jkl'):
            print("validateFloat fails with bad stringed float 'abc3def2ghi.5jkl'")
            errors += 1

    if not hasattr(common, 'validateFloatToString'):
        print("Missing attribute validateFloatToString")
        errors += 1
    else:
        if not checkFunctionality('32.5', common.validateFloat, 32.5):
            print("validateFloatToString fails with normal float 32.5")
            errors += 1
        if not checkFunctionality('32.5', common.validateFloat, '32.5'):
            print("validateFloatToString fails with stringed float '32'")
            errors += 1
        if not checkFunctionality('32.5', common.validateFloat, 'abc3def2ghi.5jkl'):
            print("validateFloatToString fails with bad stringed float 'abc3def2ghi.5jkl'")
            errors += 1

    # if not hasattr(common, 'validateFloats'):
    #     print("Missing attribute validateFloats")
    #     errors += 1
    # else:
    #     if not checkFunctionality([32, 64], common.validateFloats, ['stuff', 32.5, 64.5])
    #         print("validateFloats fails with ['stuff', 32.5, 64.5]")
    #         errors += 1
    #     if not checkFunctionality([32, 64], common.validateFloats, [32.5, 64.5]):
    #         print("validateFloats fails with [32.5, 64.5]")
    #         errors += 1

    if not hasattr(common, 'convertibleToInteger'):
        print("Missing attribute convertibleToInteger")
        errors += 1
    else:
        if not checkFunctionality(True, common.convertibleToInteger, 32):
            print("convertibleToInteger fails with int 32")
            errors += 1
        if not checkFunctionality(True, common.convertibleToInteger, '32'):
            print("convertibleToInteger fails with stringed int '32'")
            errors += 1
        if not checkFunctionality(True, common.convertibleToInteger, 'abc32def'):
            print("convertibleToInteger fails with bad stringed int 'abc32def'")
            errors += 1
        if not checkFunctionality(False, common.convertibleToInteger, 'stuff'):
            print("convertibleToInteger fails with string 'stuff'")
            errors += 1

    if not hasattr(common, 'convertibleToFloat'):
        print("Missing attribute convertibleToFloat")
        errors += 1
    else:
        if not checkFunctionality(True, common.convertibleToFloat, 32):
            print("convertibleToFloat fails with int 32")
            errors += 1
        if not checkFunctionality(True, common.convertibleToFloat, '32'):
            print("convertibleToFloat fails with stringed int '32'")
            errors += 1
        if not checkFunctionality(True, common.convertibleToFloat, 'abc32def'):
            print("convertibleToFloat fails with bad stringed int 'abc32def'")
            errors += 1
        if not checkFunctionality(False, common.convertibleToFloat, 'stuff'):
            print("convertibleToFloat fails with string 'stuff'")
            errors += 1

    print("Finished with", str(errors), "error(s).", (" I swear it's not my fault." if errors > 0 else ''))

def checkFactor():
    import factor

def checkFactorPairs():
    import factorpairs

def checkGcf():
    import gcf

def checkPerfect():
    import perfect

def checkRoot():
    import root

### Add custom checking functions between this comment and the next one.



### Add them to the bottom of the list. The key should be the module's name in lowercase.

modList = {
    'all': checkAll,
    'common': checkCommon,
    'factor': checkFactor,
    'factorpairs': checkFactorPairs,
    'gcf': checkGcf,
    'perfect': checkPerfect,
    'root': checkRoot
}

def checkAll():
    for i in modList[1:]:
        modList[i]()


if __name__ == "__main__":
    try:
        input = argv[1:]
    except IndexError:
        print("Usage: test.py module|all [module 2...]")
    
    toCheck = list(filter(lambda x: True if x in modList else False, input))
    mismatch = list(filter(lambda x: False if x in modList else True, input))

    if len(mismatch) > 0: 
        print("Inputs did not match any modules:", ', '.join(mismatch))
    
    for i in toCheck:
        modList[toCheck]()