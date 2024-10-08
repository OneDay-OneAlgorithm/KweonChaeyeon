import sys

input = sys.stdin.readline
n = int(input())

d = [[0] * 3 for _ in range(n + 1)]
d[1] = [1] * 3

for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1] + d[i - 1][2]
    d[i][1] = d[i - 1][0] + d[i - 1][2]
    d[i][2] = d[i - 1][0] + d[i - 1][1]
    for j in range(3):
        d[i][j] %= 9901

print(sum(d[n]) % 9901)