import sys

input = sys.stdin.readline

check = [False] * 1000001
check[0] = check[1] = True
prime = []

for i in range(2, 1000001):
    if check[i] == False:
        prime.append(i)
        j = i * 2
        while j <= 1000000:
            check[j] = True
            j += i
        
while True:
    n = int(input())
    
    if n == 0:
        break
    
    for a in prime:
        if check[a] == False and check[n - a] == False:
            print(f"{n} = {a} + {n - a}")
            break
    