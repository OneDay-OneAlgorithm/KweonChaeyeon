# import sys

# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().strip().split()))

# result = [-1 for i in range(N)]
# freq = [0 for i in range(1000001)]
# stack = []

# for i in A:
#     freq[i] += 1

# for index in range(N):
#     while stack and freq[A[stack[-1]]] < freq[A[index]]:
#         result[stack.pop()] = A[index]
#     stack.append(index)

# print(' '.join(map(str, result)))

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

f = [0] * 1000001
for i in range(n):
    f[a[i]] += 1
    
result = [-1] * n
stack = []
for i in range(n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(' '.join(map(str, result)))