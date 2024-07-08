import sys

input = sys.stdin.readline

sentence = input().strip()

stack = []
count = 0
index = 0

for i in sentence:
    if i == '(':
        stack.append(index)
    elif i == ')':
        if (stack[-1] == index - 1):
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
            
    index += 1
    
print(count)