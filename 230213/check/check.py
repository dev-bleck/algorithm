import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = input()
    stack = []
    status = 1

    for i in s:
        if i == '(' or i == '{':
            stack.append(i)

        if len(stack) != 0 and i == '}':
            if stack.pop() == '{':
                continue
        elif len(stack) != 0 and i == ')':
            if stack.pop() == '(':
                continue
        elif len(stack) == 0:
            status = 0

    print(f'#{test_case} {status} {s}')
    # for idx in range(len(s)):
    #     if s[idx] == '(' or s[idx] == ')' or \
    #             s[idx] == '{' or s[idx] == '}':
    #         stack.append(s[idx])
    #
    # if (stack[0] == '(' or stack[0] == '{')\
    #         and stack.count('(') == stack.count(')')\
    #         and stack.count('{') == stack.count('}'):
    #     print(f'#{test_case} 1')
    # else:
    #     print(f'#{test_case} 0')

    # for i in range(len(stack)):
    #     if (stack[i] == '(' and stack[i+1] == ')') or (stack[i] == '{' and stack[i+1] == '}'):
    # print("".join(stack))
    # print(f'{s} {stack}')
