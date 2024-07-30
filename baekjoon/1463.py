# dp - top-down
# import sys
# sys.setrecursionlimit(10**7)

# input = sys.stdin.readline
# N = int(input())
# d = [0] * (N + 1)

# def dp(n):
#     if n == 1:
#         return 0
#     if d[n] > 0:
#         return d[n]
#     count = dp(n - 1) + 1
#     if (n % 3 == 0):
#         temp = dp(n // 3) + 1
#         if count > temp: count = temp
#     if (n % 2 == 0):
#         temp = dp(n // 2) + 1
#         if count > temp: count = temp
#     d[n] = count
#     return d[n]

# print(dp(N))

# dp - bottom-up
import sys

input = sys.stdin.readline
N = int(input())
d = [0] * (N + 1)

for i in range(2, N + 1):
    count = d[i - 1] + 1
    if (i % 3 == 0):
        temp = d[i // 3] + 1
        if count > temp: count = temp
    if (i % 2 == 0):
        temp = d[i // 2] + 1
        if count > temp: count = temp
    d[i] = count

print(d[N])