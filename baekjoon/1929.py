# import sys

# input = sys.stdin.readline

# M, N = list(map(int, input().split()))

# check = [False] * (N + 1) # 소수가 아님을 체크하면 True로 변경

# for i in range(2, N + 1):
#     if check[i] == False:
#         if i >= M and i <= N:
#             print(i)
#         j = i * 2
#         while j <= N:
#             check[j] = True
#             j += i
            
import sys

input = sys.stdin.readline

M, N = list(map(int, input().split()))

prime = []
check = [False] * (N + 1) # 소수가 아님을 체크하면 True로 변경

for i in range(2, N + 1):
    if check[i] == False:
        if i >= M and i <= N:
            prime.append(i)
        j = i * 2
        while j <= N:
            check[j] = True
            j += i
            
print('\n'.join(map(str, prime)))