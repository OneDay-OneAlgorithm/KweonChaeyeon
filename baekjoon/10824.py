import sys

input = sys.stdin.readline

e = input().split()

AB = e[0] + e[1]
CD = e[2] + e[3]

print(int(AB) + int(CD))