# # 이차원 배열 이용
# import sys

# input = sys.stdin.readline
# n = int(input())

# d = [[0] * 2 for _ in range(n + 1)]

# for i in range(1, n + 1):
#     d[i][0] = d[i - 1][0] + d[i - 1][1]
#     d[i][1] = d[i - 1][0]
#     if i == 1:
#         d[1][1] = 1
        
# print(sum(d[n]))

# 일차원 배열 이용
import sys

input = sys.stdin.readline
n = int(input())

d = [0] * (n + 1)
d[1] = 1

for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])