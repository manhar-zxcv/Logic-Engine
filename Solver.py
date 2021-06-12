def solveCNF(lst):
    lst1,variable = [],set()
    for cnf in lst:
        se,allset = set(),set()
        for letter in cnf:
            z = letter.swapcase()
            if letter.lower() not in variable:
                variable.add(letter.lower())
            if z in se:
                se.remove(z)
            elif letter not in allset:
                se.add(letter)
                allset.add(letter)
        if len(se):
            lst1.append(list(se))
    fixed,flag = {},1
    # 1 : True (lower) ; 0 : False (upper)
    while flag:
        flag = 0
        for cnf in lst1:
            if len(cnf) == 1:
                letter = cnf[0]
                if letter.isupper():
                    z = letter.lower()
                    val = fixed.get(z)
                    if val == 1:
                        return []
                    elif val == None:
                        flag = 1
                    fixed[z] = 0
                else:
                    val = fixed.get(letter)
                    if val == 0:
                        return []
                    elif val == None:
                        flag = 1
                    fixed[letter] = 1
        lst2 = []
        for cnf in lst1:
            se = []
            for letter in cnf:
                isPresent = fixed.get(letter)
                if (isPresent == 1 and letter.islower()) or (isPresent == 0 and letter.isupper()):
                    break
                if isPresent == None and fixed.get(letter.swapcase()) == None:
                    se.append(letter)
            else:
                if len(se):
                    lst2.append(se)
        lst1 = lst2
    for letter in fixed:
        variable.remove(letter)
    variable = sorted(variable)
    answer = []
    for bitmask in range(1<<len(variable)):
        value,mask = {},1
        for _ in range(len(variable)):
            if bitmask&mask:
                value[variable[_]] = 1
            else:
                value[variable[_]] = 0
            mask <<= 1
        for cnf in lst1:
            if not any(map(lambda xx:value[xx] if xx.islower() else value[xx.lower()]^1,cnf)):
                break
        else:
            value.update(fixed)
            answer.append(value)
    return answer

def solveProp(lst):
    variable = set()
    for prop in lst:
        for letter in prop:
            z = letter.lower()
            if 97 <= ord(z) <= 122:
                variable.add(z)

    variable = sorted(variable)
    TruthTable = {'&':[0,0,0,1],'|':[0,1,1,1],'#':[1,0,1,1],'@':[1,0,0,1]}
    # operator ; left operand + right operand*2
    answer = []
    for bitmask in range(1<<len(variable)):
        value,mask = {},1
        for _ in range(len(variable)):
            if bitmask&mask:
                value[variable[_]] = 1
            else:
                value[variable[_]] = 0
            mask <<= 1
        for prop in lst:
            stack = []
            for letter in prop:
                lowerletter = letter.lower()
                z = value.get(lowerletter) if letter == lowerletter else value.get(lowerletter)^1
                if letter == '~':
                    stack.append(letter)
                elif z == None:
                    b,a = stack.pop(),stack.pop()
                    if a == '~':
                        b ^= 1
                        a = stack.pop()
                    stack.append(TruthTable[letter][a+b+b])
                else:
                    stack.append(z)
            if stack[0] == '~':
                ans = stack[1]^1
            else:
                ans = stack[0]
            if not ans:
                break
        else:
            answer.append(value)
    return answer