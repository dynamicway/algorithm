def is_valid_ps(s):
    if len(s) & 1 == 1:
        return False
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                return False
            stack.pop()
    return len(stack) == 0
