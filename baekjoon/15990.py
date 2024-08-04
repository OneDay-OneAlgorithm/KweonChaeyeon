import sys

d = [[0] * 4 for _ in range(100001)]

for i in range(1, 100001):
    if i - 1 >= 0:
        d[i][1] = d[i - 1][2] + d[i - 1][3]
        if i == 1:
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i - 2][3] + d[i - 2][1]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i - 3][1] + d[i - 3][2]
        if i == 3:
            d[i][3] = 1
        
    d[i][1] %= 1000000009
    d[i][2] %= 1000000009
    d[i][3] %= 1000000009
                
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    count = 0
    n = int(input())
    count = d[n][1] + d[n][2] + d[n][3]
    print(count % 1000000009)