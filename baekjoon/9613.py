import sys

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    value = input().split()
    value_list = list(map(int, value))
    
    n = value_list[0]
    elements = value_list[1:]
    
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            result += GCD(elements[i], elements[j])
    
    print(result)