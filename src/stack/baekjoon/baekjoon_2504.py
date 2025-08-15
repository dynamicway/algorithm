def calculate(s):
    if len(s) & 1 == 1:
        return 0

    values = {')': 2, ']': 3}
    stack = []
    for char in s:
        if char in '([':
            stack.append(char)
        else:
            temp = 0
            while stack and isinstance(stack[-1], int):
                temp += stack.pop()
            if not stack or not is_pair_of(stack[-1], char):
                return 0
            stack.pop()
            stack.append(max(values[char], temp * values[char]))
            
    result = 0
    while len(stack) != 0:
        cur = stack.pop()
        if not isinstance(cur, int):
            return 0
        result += cur

    return result
    
def is_pair_of(c1, c2):
    if '(' == c1 and c2 == ')':
        return True
    if '[' == c1 and c2 == ']':
        return True
    return False
