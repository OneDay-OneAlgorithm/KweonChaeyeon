import sys

input = sys.stdin.readline

sentence = input().strip()

tagOpen = False
stack = []

for i in sentence:
    if i == '<':
        while (stack):
            print(stack.pop(), end = '')
        tagOpen = True
        print('<', end = '')
    elif i == '>':
        tagOpen = False
        print('>', end = '')
    elif tagOpen == True:
        print(i, end = '')
    elif tagOpen == False and i != ' ':
        stack.append(i)
    else:
        while (stack):
            print(stack.pop(), end = '')
        print(' ', end = '')

# 스택이 비어 있지 않은 경우 체크
while (stack):
    print(stack.pop(), end = '')    
print('')
        
    