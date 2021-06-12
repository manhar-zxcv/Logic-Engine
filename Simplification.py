def simplifyProp(lst):
    ans = []
    for string in lst:
        curr = []
        for letter in string:
            if letter == '~':
                if len(curr) and curr[-1] == '~':
                    curr.pop()
                else:
                    curr.append(letter)
            else:
                curr.append(letter)
        ans.append(''.join(curr))
    ans1 = []
    precedence = {'&':4,'|':3,'#':2,'@':1,'(':-1,')':-1}
    for string in ans:
        operatorStack = []
        final = []
        for index,letter in enumerate(string):
            if letter == '~':
                final.append(letter)
            elif not precedence.get(letter):
                if len(final) and string[index-1] == '~':
                    final.pop()
                    final.append(letter.upper())
                else:
                    final.append(letter)
            else:
                if letter == '(':
                    operatorStack.append(letter)
                elif letter == ')':
                    while operatorStack[-1] != '(':
                        final.append(operatorStack.pop())
                    operatorStack.pop()
                else:
                    while len(operatorStack) and precedence[operatorStack[-1]] >= precedence[letter]:
                        final.append(operatorStack.pop())
                    operatorStack.append(letter)
        ans1.append(''.join(final))
    return ans1

def SimplifyCNF(lst):
    ans = []
    for string in lst:
        curr = []
        for letter in string:
            if letter == '(':
                curr = []
            elif letter == ')':
                ans.append(''.join(curr).split('|'))
            elif letter == '~':
                if len(curr) and curr[-1] == '~':
                    curr.pop()
                else:
                    curr.append(letter)
            else:
                if len(curr) and curr[-1] == '~':
                    curr.pop()
                    curr.append(letter.upper())
                else:
                    curr.append(letter)
    return ans