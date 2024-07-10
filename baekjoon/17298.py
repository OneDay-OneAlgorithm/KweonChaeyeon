import sys

input = sys.stdin.readline

N = int(input())

A = input().split()
elements = list(map(int, A))

stack = []
result = [-1] * N

for index in range(N):
    while stack and elements[stack[-1]] < elements[index]:
        result[stack.pop()] = elements[index]
    stack.append(index)
    
print(' '.join(map(str, result)))
        