# import sys

# input = sys.stdin.readline

# def sticker(n, a):
#     d = [[0] * 3 for _ in range(n + 1)]
    
#     for i in range(1, n + 1):
#         d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
#         d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[0][i]
#         d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[1][i]
    
#     score = max(d[n][0], d[n][1], d[n][2])
#     return score

# t = int(input())
# for _ in range(t):
#     n = int(input())
    
#     a = [[0] * (n + 1) for _ in range(2)]
#     for i in range(2):
#         a[i][1:] = list(map(int, input().split()))
    
#     print(sticker(n, a))
    
import sys

input = sys.stdin.readline

def sticker(n, a):
    d = [[0] * 3 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[i][0]
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[i][1]
    
    score = max(d[n][0], d[n][1], d[n][2])
    return score

t = int(input())
for _ in range(t):
    n = int(input())
    
    scores1 = [0] + list(map(int, input().split()))
    scores2 = [0] + list(map(int, input().split()))
    a = list(zip(scores1, scores2))
    
    print(sticker(n, a))