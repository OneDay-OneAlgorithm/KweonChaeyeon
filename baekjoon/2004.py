import sys

def calc(n, v):
    count = 0
    i = v
    
    while v <= n:
        count += n // v
        v *= i
    return count

input = sys.stdin.readline
n, m = map(int, input().split())

# v가 2일 경우
result_2 = calc(n, 2) - calc(n - m, 2) - calc(m, 2)

# v가 5일 경우    
result_5 = calc(n, 5) - calc(n - m, 5) - calc(m, 5)

print(min(result_2, result_5))
        