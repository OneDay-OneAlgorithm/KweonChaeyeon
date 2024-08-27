import sys

input = sys.stdin.readline
s = input().strip()

alpha = [0] * 26
a = ord('a')
for c in s:
    alpha[ord(c) - a] += 1

print(' '.join(map(str, alpha)))