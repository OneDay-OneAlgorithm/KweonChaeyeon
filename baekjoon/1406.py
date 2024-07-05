import sys

input = sys.stdin.readline

sentence = input().strip()
M = int(input())

left_stack = []
right_stack = []

left_stack = list(sentence) # 문자열을 list로 치환
for _ in range(M):
    command = input().strip().split()
    
    if (command[0] == 'L'):
        if (left_stack):
            word = left_stack.pop()
            right_stack.append(word)
    elif (command[0] == 'D'):
        if (right_stack):
            word = right_stack.pop()
            left_stack.append(word)
    elif (command[0] == 'B'):
        if (left_stack):
            left_stack.pop()
    else: # P $ 명령어가 들어온 경우
        left_stack.append(command[1])
        
result = ''.join(left_stack + right_stack[::-1]) # ::-1 -> 역순으로 출력
    
print(result)