# import sys

# input = sys.stdin.readline

# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# a_abs = [abs(i - s) for i in a]

# def GCD(a, b):
#     if b == 0:
#         return a
#     else:
#         return GCD(b, a % b)

# gcd = 0
# if len(a_abs) == 1:
#     print(a_abs[0])
# else:
#     gcd = GCD(a_abs[0], a_abs[1])
#     for i in range(2, n):
#         gcd = GCD(gcd, a_abs[i])
#     print(gcd)

import sys
import math

input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
a_abs = [abs(i - s) for i in a]

gcd = a_abs[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a_abs[i])

print(gcd)