# import sys

# input = sys.stdin.readline

# sentence = input().strip()

# stack = []
# count = 0
# index = 0

# for i in sentence:
#     if i == '(':
#         stack.append(index)
#     elif i == ')':
#         if (stack[-1] == index - 1):
#             stack.pop()
#             count += len(stack)
#         else:
#             stack.pop()
#             count += 1
            
#     index += 1
    
# print(count)

import sys

input = sys.stdin.readline

t = input().strip()

result = 0
bar = 0
laser = 0

for i in range(len(t)):
    if t[i] == '(':
        bar += 1
    elif t[i] == ')' and t[i - 1] != '(':
        bar -= 1
        result += 1
    elif t[i] == ')' and t[i - 1] == '(':
        bar -= 1
        result += bar
        
print(result)