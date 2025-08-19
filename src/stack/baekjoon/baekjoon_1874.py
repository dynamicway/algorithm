import sys

def generate_stack_operations(n, sequence):
    result = []

    stack1 = list(range(n, 0, -1))
    stack2 = []

    for s in sequence:
        if len(stack2) == 0:
            stack2.append(stack1.pop())
            result.append("+")

        if stack2[-1] > s:
            raise ValueError("Impossible sequence")

        while stack2[-1] != s:
            stack2.append(stack1.pop())
            result.append("+")

        stack2.pop()
        result.append("-")

    return result

# input = sys.stdin.readline
# print = sys.stdout.write

# sequence = []
# n = int(input())
# for i in range(n):
#     sequence.append(int(input()))

# try:
#     operations = generate_stack_operations(n, sequence)
#     for op in operations:
#         print(op + "\n")
# except ValueError as e:
#     if str(e) != "Impossible sequence":
#         raise
#     print("NO")
    
    

