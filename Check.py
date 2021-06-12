from string import ascii_lowercase

alphabets = set(ascii_lowercase)
specialSymbolsProp = set('&|#@')
specialSymbolsCNF = set('&|')

def checkParenthisis(string):
    st = 0
    for char in string:
        st += 1 if char=='(' else -1 if char == ')' else 0
        if st < 0:
            return 1
    return st

def checkLiteral(string):
    for char in string:
        if char in alphabets:
            return 0
    return 1

def checkFormatProp(string):
    if string[0] in specialSymbolsProp:
        return 1
    for i in range(len(string)):
        if (string[i] in specialSymbolsProp or string[i] == '(') and \
        (i == len(string)-1 or string[i+1] in specialSymbolsProp or string[i+1] == ')'):
            return 1
    for i in range(len(string)-1):
        if (string[i] in alphabets or string[i] == ')') and \
        (string[i+1] not in specialSymbolsProp and string[i+1] != ')'):
            return 1
    for i in range(len(string)):
        if string[i] == '~' and (i == len(string)-1 or
        (string[i+1] not in alphabets and string[i+1] != '(' and string[i+1] != '~')):
            return 1
    return 0

def checkFormatCNF(string):
    if string[0] in specialSymbolsCNF or string[0] == '~':
        return 1
    for i in range(len(string)):
        if (string[i] == '|' or string[i] == '(') and \
        (i == len(string)-1 or string[i+1] in specialSymbolsCNF or string[i+1] in '()'):
            return 1
        if (string[i] == '&') and (i == len(string)-1 or string[i+1] != '('):
            return 1
    for i in range(len(string)-1):
        if (string[i] in alphabets or string[i] == ')') and \
        (string[i+1] not in specialSymbolsCNF and string[i+1] != ')'):
            return 1
    for i in range(len(string)):
        if string[i] == '~' and (i == len(string)-1 or
        (string[i+1] not in alphabets and string[i+1] != '(' and string[i+1] != '~')):
            return 1
    return 0