import sys

input = sys.stdin.readlines
s_list = input()

for s in s_list:
    result = [0] * 4
    for c in s:
        if 'a' <= c <= 'z':
            result[0] += 1
        elif 'A' <= c <= 'Z':
            result[1] += 1
        elif '0' <= c <= '9':
            result[2] += 1
        elif c == ' ':
            result[3] += 1
    print(' '.join(map(str, result)))