import sys

input = sys.stdin.readline # sys.stdin.readline()과 동일한 속도를 가짐
n = int(input())

stack = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    if cmd == 'push':
        num = int(s[1])
        stack.append(num)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack: # 리스트 stack이 비어 있으면 false, 비어 있지 않으면 true
            print(0)
        else:
            print(1)
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)