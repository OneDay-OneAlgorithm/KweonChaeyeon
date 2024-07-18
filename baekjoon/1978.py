import sys

input = sys.stdin.readline
N = int(input())
inputs = list(map(int, input().split()))

count = 0
for i in inputs:
    if (i < 2):
        continue
    
    k = 2
    prime = True
    while k * k <= i:
        if  i % k == 0:
            prime = False
            break
        k += 1
    
    if prime == True:
        count += 1
    
print(count)