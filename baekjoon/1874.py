import sys

input = sys.stdin.readline
n = int(input())

stack = []
result = []
base = 0
for _ in range(n):
    t = int(input())
    while base < t:
        base += 1
        stack.append(base)
        result.append("+")
    if not stack:
        result.clear()
        print("NO")
        break
    else:
        top = stack.pop()
        if t == top:
            result.append("-")
        else:
            result.clear()
            print("NO")
            break

if result:
    print(*result, sep='\n')
        