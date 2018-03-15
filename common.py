def validateInteger(input):
    validatedString = ""
    rawString = str(input)

    if rawString.startswith('-'):
        validatedString += '-'

    for char in rawString:
        if char.isdigit():
            validatedString += char
    return int(validatedString)

def validateIntegers(input):
    return list(map(validateInteger, list(filter(lambda x: convertibleToInteger(x), input))))

def validateFloats(input):
    return list(map(validateFloat, list(filter(lambda x: convertibleToFloat(x), input))))

def validateFloat(input):
    validatedString = ""
    rawString = str(input)
    oneDecimal = False
    
    if rawString.startswith('-'):
        validatedString += '-'

    for char in rawString:
        if char.isdigit()or char == '.':
            if char == '.' and not oneDecimal:
                validatedString += char
                oneDecimal = True
            else:
                validatedString += char
    try:
        rv = float(validatedString)
    except ValueError:
        rv = None
    return rv

def validateIntegerToString(input):
    return str(validateInteger(input))

def validateFloatToString(input):
    return str(validateFloat(input))

def hasDigits(input):
    rawString = str(input)
    
    if rawString == "":
        return False
    for char in rawString:
        if not char.isdigit():
            return False
    return True

def convertibleToInteger(input):
    rawString = str(input)
    if len(input) == 0:
        return False

    for char in rawString:
        if char.isdigit():
            return True
    return False

def convertibleToFloat(input):
    pass

def checkFloatEven(input):
    if validateFloat(input) == validateFloat(validateIntegerToString(input) + '.0'):
        return True
    return False