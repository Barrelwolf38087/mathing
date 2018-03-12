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