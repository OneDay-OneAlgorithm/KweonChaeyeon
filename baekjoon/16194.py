import sys

input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] + [-1] * (n)

# for i in range(1 , n + 1):
#     for j in range(1, i + 1):
#         if d[i] == -1:
#             d[i] = d[i - j] + p[j]
#         else:
#             d[i] = min(d[i], d[i -j] + p[j])

for i in range(1 , n + 1):
    for j in range(1, i + 1):
        if d[i] == -1 or d[i] > d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
            
print(d[n])