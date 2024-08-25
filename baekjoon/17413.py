# import sys

# input = sys.stdin.readline

# sentence = input().strip()

# tagOpen = False
# stack = []

# for i in sentence:
#     if i == '<':
#         while (stack):
#             print(stack.pop(), end = '')
#         tagOpen = True
#         print('<', end = '')
#     elif i == '>':
#         tagOpen = False
#         print('>', end = '')
#     elif tagOpen == True:
#         print(i, end = '')
#     elif tagOpen == False and i != ' ':
#         stack.append(i)
#     else:
#         while (stack):
#             print(stack.pop(), end = '')
#         print(' ', end = '')

# # 스택이 비어 있지 않은 경우 체크
# while (stack):
#     print(stack.pop(), end = '')    
# print('') 

import sys

input = sys.stdin.readline

s = list(input())

stack = []
result = ''
tag_flag = False
for i in range(len(s) - 1):
    if s[i] != '<' and tag_flag == False:
        if s[i] != ' ':
            stack.append(s[i])
        if s[i] == ' ' or s[i + 1] == '<' or s[i + 1] == '\n':
            while stack:
                result += stack.pop()
            if s[i] == ' ':
                result += ' '
    elif s[i] ==  '<' or tag_flag == True:    
        result += s[i]
        if s[i] == '<':
            tag_flag = True
        elif s[i] == '>':
            tag_flag = False
print(result)