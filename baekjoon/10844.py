import sys

d = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, 101):
    for j in range(0, 10):
        if j >= 1:
            d[i][j] += d[i - 1][j - 1]
        if j <= 8:
            d[i][j] += d[i - 1][j + 1]
        d[i][j] %= 1000000000
    
input = sys.stdin.readline
n = int(input())
result = 0
for i in range(0, 10):
    result += d[n][i]
    
print(result % 1000000000)