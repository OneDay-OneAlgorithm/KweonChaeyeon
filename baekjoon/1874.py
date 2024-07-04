import sys

input = sys.stdin.readline
T = int(input())

element = 0
stack = []
result = []

for _ in range(T):
    num = int(input())
    
    if element < num:
        while element < num:
            element += 1
            stack.append(element)
            result.append('+')
        stack.pop()
        result.append('-')
    else: # element > num일 경우(element == num은 나오지 않을 거임)
        if (stack[-1] != num):
            print('NO')
            sys.exit(0)
        top = stack.pop()
        result.append('-')
          
print('\n'.join(result))
        