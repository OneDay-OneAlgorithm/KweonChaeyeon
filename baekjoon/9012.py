import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    stack = []
    line = input()
    
    result = "YES"
    for c in line:
        if c == '(':
           stack.append(c)
        elif c == ')':
            if not stack:
                result = "NO"
            else:
                stack.pop()
    if len(stack) != 0:
        result = "NO"
    print(result)