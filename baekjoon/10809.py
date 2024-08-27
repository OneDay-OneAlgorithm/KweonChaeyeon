import sys

input = sys.stdin.readline
s = input().strip()

alpha = [-1] * 26
a = ord('a')
for i in range(len(s)):
    if alpha[ord(s[i]) - a] == -1:
        alpha[ord(s[i]) - a] = i

print(' '.join(map(str, alpha)))