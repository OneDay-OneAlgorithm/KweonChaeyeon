import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(0, n):
    d[i] = a[i]
    if d[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]

print(max(d))