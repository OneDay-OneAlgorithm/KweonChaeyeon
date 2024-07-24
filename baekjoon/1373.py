# import sys

# input = sys.stdin.readline

# value = list(map(int, list(input().strip())))

# multi = [1, 2, 4]
# multi_index = 0
# sum = 0
# result = ''

# for i in reversed(value):
#     if multi_index >= 3:
#         result += str(sum)
#         sum = 0
#         multi_index = 0
    
#     sum += i * multi[multi_index]
    
#     multi_index += 1
# print(str(sum) + result[::-1])
# -------------------------------------------------------------------------

# import sys

# input = sys.stdin.readline

# s = input().strip()
# n = len(s)
# result = ''

# if n % 3 == 1:
#     print(s[0], end = '')
# elif n % 3 == 2:
#     print((ord(s[0]) - ord('0')) * 2 + (ord(s[1]) - ord('0')), end = '')

# for i in range(n % 3, n, 3):
#     print((ord(s[i]) - ord('0')) * 4 + (ord(s[i + 1]) - ord('0')) * 2 + (ord(s[i + 2]) - ord('0')), end = '')
# -------------------------------------------------------------------------

import sys

input = sys.stdin.readline

n = input().strip()

b = int(n, 2) # 2진수에서 10진수로 변환
print(oct(b)[2:]) # 10진수에서 8진수로 변환 -> 앞에 0o 떼고 출력