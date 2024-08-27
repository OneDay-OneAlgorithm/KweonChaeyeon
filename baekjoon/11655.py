import sys

input = sys.stdin.readline
s = list(input())

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        encrypt_ord = ord(s[i]) + 13
        if encrypt_ord > Z:
            encrypt_ord = A + encrypt_ord % Z - 1
        s[i] = chr(encrypt_ord)
    elif 'a' <= s[i] <= 'z':
        encrypt_ord = ord(s[i]) + 13
        if encrypt_ord > z:
            encrypt_ord = a + encrypt_ord % z - 1
        s[i] = chr(encrypt_ord)

print(''.join(s), end = '')