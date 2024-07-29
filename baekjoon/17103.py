import sys

# 에라토스테네스의 체
max_n = 1000000
g = [False] * (max_n + 1)
g[0] = g[1] = True
primes = []
for i in range(2, max_n + 1):
    if g[i] == False:
        primes.append(i)
        j = i * 2
        while j <= max_n:
            if g[j] == False:
                g[j] = True
            j += i

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    result = 0
    n = int(input())
    
    for i in primes:
        if i <= n - i:
            if g[n - i] == False:
                result += 1
        else:
            break
    print(result)