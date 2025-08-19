from collections import deque

def find_last_card(n):
    dq = deque(range(1, n + 1))
    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())
    return dq.popleft()
