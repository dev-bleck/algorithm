import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, 11):
    _ = int(input())
    expression = input()
    stack = []
    result_expr = ''  # 후위표기법으로 완성된 식

    # 1. 숫자 -> 출력
    # 2. 연산자
    # 2-1. 나보다 쌔거나 같다 -> pop
    # 2-2. 나보다 약하다 -> push

    for token in expression:
        # 숫자다
        if token not in '*+':
            # 출력
            result_expr += token
        # 연산자다
        else:
            # 스택이 비어있으면
            if not stack:
                stack.append(token)
            elif token in "*":
                # 나보다 우선순위가 높거나 같은애가 제일 위에 있다
                while stack and stack[-1] in "*":
                    # 출력해준다
                    result_expr += stack.pop()
                # pop이 끝나면 들어간다
                stack.append(token)
            elif token in "+":
                while stack:
                    result_expr += stack.pop()
                stack.append(token)

    # stack을 비워서 연산자 마저 출력
    while stack:
        result_expr += stack.pop()

    # 후위 표기법으로 표현된 수식 계산 시작
    # 1. 숫자는 stack에 push
    # 2. 연산자는 stack에서 pop 2번
    for token in result_expr:
        # 숫자라면
        if token not in "*+":
            # stack에 push
            stack.append(int(token))
        # 연산자가 나오면
        else:
            # 오류 검증 코드인데 지금은 안써도 됨
            if len(stack) < 2:
                break
            right_operand = stack.pop()
            left_operand = stack.pop()
            if token == "+":
                stack.append(left_operand + right_operand)
            elif token == "*":
                stack.append(left_operand * right_operand)

    # 남은 숫자가 하나가 아니라면
    if len(stack) != 1:
        # 오류임
        pass
    else:
        print(f'#{test_case}', *stack)