import sys

input = sys.stdin.readline
n = int(input())

a = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    a[i] = int(input())

d[1] = a[1]
if n >= 2:
    d[2] = a[1] + a[2]
    
for i in range(3, n + 1):
    t1 = a[i] + a[i - 1] + d[i - 3]
    t2 = a[i] + d[i - 2]
    t3 = d[i - 1]
    
    d[i] = max(t1, t2, t3)
    
print(d[n])