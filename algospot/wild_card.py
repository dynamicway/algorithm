def match(w, str):
    if len(w) == 0:
        return False

    sw = split_wildcard(w)
    return solve(0, str, sw)

def split_wildcard(w):
    result = []
    current = ''
    for char in w:
        current += char
        if char == '*':
            result.append(current)
            current = ''

    if current != '':
        result.append(current)
    return result

def solve(idx, str, sw):
    if idx == len(sw):
        return True
    w = sw[idx]

    if not startsWith(str, w):
        return False
    
    for s in range(len(str)):
        if solve(idx + 1, str[len(w) - 1 + s:], sw):
            return True
    return False

def startsWith(str, w):
    if w == '*':
        return True
    if len(str) < len(w[:-1]):
        return False
    
    if w[-1] != '*':
        return str == w
    
    for i in range(len(w[:-1])):
        if w[i] != '?' and str[i] != w[i]:
            return False
    return True
