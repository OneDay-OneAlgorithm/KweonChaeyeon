import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    sentence = input().strip() # 문자열 앞, 뒤의 공백 문자를 제거
    
    stack_size = 0
    is_finished = False
    for i in sentence:
        if i == '(':
            stack_size += 1
        else:
            if stack_size == 0: # 여는 괄호가 부족함
                print('NO')
                is_finished = True
                break
            stack_size -= 1

    # 이미 위에서 출력한 경우 체크
    if is_finished == True:
        continue
    if stack_size == 0:
        print('YES')
    else: # 닫는 괄호가 부족함
        print('NO')
    