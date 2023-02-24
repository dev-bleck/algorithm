import sys
sys.stdin = open('sample_input.txt')

# 이러면 계산은 끝이긴 하지만...
# for test_case in range(1, 11):
#     _, expression = int(input()), input()
#     print(f'#{test_case} {eval(expression)}')


for test_case in range(1, 11):
    # 중위 표기식
    _, expression = int(input()), input()
    # 후위 표기식
    result = ''
    # 연산자 저장용 스택
    stack = []
    for token in expression:
        # token이 연산자(+)일 때
        if token == '+':
            # 다 같은 연산자이기 때문에 비어있는지만 확인
            if len(stack) == 0:
                # push
                stack.append(token)
            else:
                # TODO 후위표기 변환 중 연산자 비교
                # pop하고
                while stack:
                    result += stack.pop()
                # 현재 연산자 push
                stack.append(token)
        # token이 숫자일 대
        else:
            result += token

    # 남은 연산자 처리
    while stack:
        result += stack.pop()

    # 계산
    for token in result:
        # if token != '+':
        if token.isdecimal():
            stack.append(int(token))
        else:
            right_operand = stack.pop()  # 먼저 꺼낸게 뒤로
            left_operand = stack.pop()  # 나중에 꺼낸게 앞으로
            # TODO 후위표기 계산 방법 추가
            stack.append(left_operand + right_operand)

    print(f'#{test_case} {stack.pop()}')
