import sys

input = sys.stdin.readline

left = list(input().strip())
right = []

m = int(input())
for _ in range(m):
    t = input().split()
    
    if t[0] == 'L':
        if left:
            right.append(left.pop())
    elif t[0] == 'D':
        if right:
            left.append(right.pop())
    elif t[0] == 'B':
        if left:
            left.pop()
    elif t[0] == 'P':
        left.append(t[1])
print(''.join(left + right[::-1]))