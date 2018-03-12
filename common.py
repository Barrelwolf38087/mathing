def validateInteger(input):
    validatedString = ""
    rawString = str(input)

    if rawString.startswith('-'):
        validatedString += '-'

    for char in rawString:
        if char.isdigit():
            validatedString += char
    return int(validatedString)

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
    return float(validatedString)

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