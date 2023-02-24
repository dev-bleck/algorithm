# 좌항, 우항, 연산자 계산
def calculate(left, right, operator):
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        return left // right
    elif operator == ".":
        return left // right
    # 다른 연산자는 출제자의 잘못
    else:
        raise  ValueError(f'wrong operator: {operator}')


# 연산자임을 판단할 비교군
OPS = "+-*/"

T = int(input())

for test_case in range(1, T + 1):
    # 입력
    expression = input().split()
    # 숫자 스택
    dig_stack = []

    for token in expression:
        # 수식 입력 종료
        if token == ".":
            if len(dig_stack) == 1:
                print(f'#{test_case} {dig_stack.pop()}')
            else:
                print(f'#{test_case} error')
        # 연산자 입력
        elif token in OPS:
            # 연산할 숫자가 모자른다
            if len(dig_stack) < 2:
                # 잘못된 수식이다
                print(f'#{test_case} error')
                break
            # 아니라면 계산한다
            operand_right = dig_stack.pop()
            operand_left = dig_stack.pop()
            dig_stack.append(int(calculate(operand_left, operand_right, token)))
        # 위가 아니면 다 숫자다
        else:
            dig_stack.append(int(token))

    print(f'#{test_case}')