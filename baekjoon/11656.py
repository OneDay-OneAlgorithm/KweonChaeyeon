import sys

input = sys.stdin.readline

s = input().strip()

suffix = [0] * len(s)
for i in range(len(s)):
    suffix[i] = s[i:]
    
suffix.sort()
print('\n'.join(suffix))