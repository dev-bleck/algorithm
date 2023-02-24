expression1 = '2+3*4/5'
expression2 = '(6+5*(2-8)/2)'
expression3 = '3-2*5+4/2-2'
expression4 = '122-131*56+17/235'

# 받아올 수식 문자열
stack = []
# 출력 문자열
result = ''

# 한글자씩 알아보자
for token in expression4:
    if token.isdecimal():  # 현재 token이 숫자이면
        result += token
    else:
        # 스택이 비어있으면 => 첫 연산자
        if not stack:
            # 첫 연산자 push
            stack.append(token)
        # 열린 괄호
        elif token == '(':
            # 무조건 push
            stack.append(token)
        elif token in '*/':
            # 스택이 비어있으면 오류 발생하므로 stack(True) 조건 추가
            # 나보다 우선순위가 낮은 token이 나올 때까지
            while stack and stack[-1] in '*/':
                result += stack.pop()
            # 그다음 나
            stack.append(token)
        elif token in '+-':
            # +, - 보다 낮은 경우는 ( 밖에 없음
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # 남는 괄호는 버린다

# 아직 계산 안한 연산자
while stack:
    result += stack.pop()

print(result)