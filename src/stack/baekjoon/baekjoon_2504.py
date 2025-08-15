values = {')': 2, ']': 3}

def calculate(s):
    if len(s) & 1 == 1:
        return 0

    stack = []
    for char in s:
        if char in '([':
            stack.append(char)
        else:
            flag = False
            temp = 0
            while len(stack) != 0:
                cur = stack.pop()
                if isinstance(cur, int):
                    temp += cur
                elif isPairOf(cur, char):
                    stack.append(max(values[char], temp * values[char]))
                    flag = True
                    break
                else:
                    return 0
            if not flag:
                return 0

            if len(stack) == 0: # 지금 뭘 닫아야 하는데, 열려있는 친구가 없으니까 닫지를 못함. 따라서 0
                return 0
            
    result = 0
    while len(stack) != 0:
        cur = stack.pop()
        if not isinstance(cur, int):
            return 0
        result += cur

    return result
    
def isPairOf(c1, c2):
    if '(' == c1 and c2 == ')':
        return True
    if '[' == c1 and c2 == ']':
        return True
    return False
