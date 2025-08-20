import sys

def count_pieces(layout):
    result = 0
    stack = []

    i = 0
    while i < len(layout):
        if layout[i] == "(":
            if layout[i + 1] == "(":
                result += 1
                stack.append("(")
            else:
                result += len(stack)
                i += 1
        else:
            stack.pop()
        i += 1

    return result