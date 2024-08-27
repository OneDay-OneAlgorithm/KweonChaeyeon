import sys

input = sys.stdin.readline
infix = input().strip()

result = ''
stack = []
for c in infix:
    if 'A' <= c <= 'Z':
        result += c
    elif c == '(':
        stack.append(c)
    elif c == '*' or c == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(c)
    elif c == '+' or c == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
while stack:
    result += stack.pop()
print(result)