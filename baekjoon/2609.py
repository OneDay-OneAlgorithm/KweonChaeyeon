import sys

input = sys.stdin.readline
a, b = map(int, input().split())

# 최대공약수 구하는 함수
def GCD(a, b):
    if (b != 0):
        result = GCD(b, a % b)
    else:
        return a
    
    return result

# 최소공배수 구하는 함수
def LCM(a, b, g):
    return (a * b) // g

g = GCD(a, b)
l = LCM(a, b, g)
print(g)
print(l)