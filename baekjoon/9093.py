import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    line = input().split()
    
    for i in range(len(line)):
        line[i] = line[i][::-1]
        
    print(' '.join(line))