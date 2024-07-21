import sys

input = sys.stdin.readline

N = int(input())

i = 5
count = 0

while i <= N:
    div = N // i

    count += div
    i *= 5
    
print(count)