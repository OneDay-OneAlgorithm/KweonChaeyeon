import sys

input = sys.stdin.readline
n = int(input())

d = [[0] * (n + 1) for _ in range(n + 1)]
# a = [[0] * (n + 1) for _ in range(n + 1)]

# row = 1
# for _ in range(n):
#     a[row][1:] = list(map(int, input().split()))
#     row += 1

a = [[0] * 2]
# a 배열 > 톱니바퀴 리스트로 만들기
for _ in range(n):
    row = [0] + list(map(int, input().split())) + [0]
    a.append(row)
    
for i in range(1, n + 1):
    for j in range(1,  i + 1):
        d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + a[i][j]
        
print(max(d[n]))