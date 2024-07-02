import sys

input = sys.stdin.readline
T = int(input())

count = 1

while count <= T:
    sentence = input()
    
    stack = []
    reversedSentence = ''
    
    for i in sentence:
        if i == ' ' or i == '\n':
            while (stack):
                reversedSentence += stack.pop()
            reversedSentence += i
        else:
            stack.append(i)
    
    print(reversedSentence, end = '')
    count += 1