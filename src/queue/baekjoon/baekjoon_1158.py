from collections import deque


def josephus(n, k):
    q1 = deque(range(1, n + 1))
    q2 = deque()
    
    result = []
    while len(result) != n:
        cn = len(q1) + len(q2)
        if cn == 1:
            if q1:
                result.append(q1.popleft())
            else:
                result.append(q2.popleft())
            break
        
        remove_point = k

        if remove_point > cn:
            remove_point = remove_point % cn
        
        for i in range(k):
            if len(q1) == 0:
                q1 = q2
                q2 = deque()
            if i == k - 1:
                result.append(q1.popleft())
            else:
                q2.append(q1.popleft())

    return result

n, k = map(int, input().split())
print("<" + ", ".join(map(str, josephus(n, k))) + ">")
    