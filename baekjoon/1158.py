# O(N * K)
# import sys

# input = sys.stdin.readline

# value = input().strip().split()
# N = int(value[0])
# K = int(value[1])

# list = [i + 1 for i in range(N)]
# result = []

# index = -1
# while True:
#     if len(result) == N:
#         break
    
#     for i in range(K):
#         if index + 1 == len(list):
#             index = 0
#         else:
#             index += 1
            
#         if i == K - 1: # K번째에서 append
#             result.append(list[index])
#             del list[index]
#             index -= 1
            
# print('<' + ', '.join(map(str, result)) + '>')

# O(N * K) -> deque를 이용한 풀이
# from collections import deque
# n, m = map(int, input().split())
# q = deque()
# for i in range(1, n + 1):
#     q.append(i)
# ans = []
# for i in range(n - 1):
#     for j in range(m - 1):
#         q.append(q.popleft())
#     ans += [q.popleft()]
    
# ans += [q[0]]
# print('<' + ', '.join(map(str, ans)) + '>')

# O(N^2)
import sys

input = sys.stdin.readline

value = input().strip().split()
N = int(value[0])
K = int(value[1])

list = [i for i in range(1, N + 1)]
result = []
index = 0

for _ in range(N):
    index += K - 1
    if (index >= len(list)):
        index = index % len(list)
    result.append(list.pop(index))
    
print('<' + ', '.join(map(str, result)) + '>')