def calculate(s):
    if len(s) & 1 == 1:
        return 0

    values = {')': 2, ']': 3}
    stack = []
    for char in s:
        if char in '([':
            stack.append(char)
        else:
            sum_of_values = drain_numbers(stack)
            can_close_bracket = stack and is_pair_of(stack[-1], char)
            if not can_close_bracket:
                return 0
            stack.pop()
            stack.append(max(values[char], sum_of_values * values[char]))
            
    return sum_remaining_values(stack)
    
def is_pair_of(c1, c2):
    if '(' == c1 and c2 == ')':
        return True
    if '[' == c1 and c2 == ']':
        return True
    return False

def drain_numbers(stack):
    nested_sum = 0
    while stack and isinstance(stack[-1], int):
        nested_sum += stack.pop()
    return nested_sum
    
def sum_remaining_values(stack):
    has_unclosed_brackets = any(isinstance(item, str) for item in stack)
    if has_unclosed_brackets:
        return 0
    return sum(stack)
