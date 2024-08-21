import sys

input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    t = input().split()
    order = t[0]
    
    if order == "push":
        x = int(t[1])
        stack.append(x)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
           print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
           print(stack[-1])