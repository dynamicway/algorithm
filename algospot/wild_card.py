def match(w, str):
    if len(w) == 0:
        return False
    cache = {}

    sw = split_wildcard(w)
    return solve(0, str, sw, cache)

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

def solve(idx, str, sw, cache):
    key = (idx, str)
    if key in cache:
        return cache[key]

    if idx == len(sw):
        return True
    w = sw[idx]

    if not startsWith(str, w):
        cache[key] = False
        return False
    
    for s in range(len(str)):
        if solve(idx + 1, str[len(w) - 1 + s:], sw, cache):
            cache[key] = True
            return True
    cache[key] = False
    return False

def startsWith(str, w):
    if w[-1] == '*':
        for i in range(len(w) - 1):
            if w[i] != '?' and w[i] != str[i]:
                return False
        return True
    else:
        len_w = len(w)
        if len_w != len(str):
            return False
        for i in range(len_w):
            if w[i] != '?' and w[i] != str[i]:
                return False
        return True

