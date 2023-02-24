import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    forth = input().split()
    numb_stack = []

    for token in forth:
        if token not in '+-*/().':
            numb_stack.append(int(token))

        elif token in '+-*/.':
            try:
                if token == '+':
                    b = numb_stack.pop()
                    a = numb_stack.pop()
                    numb_stack.append(a + b)
                elif token == '-':
                    b = numb_stack.pop()
                    a = numb_stack.pop()
                    numb_stack.append(a - b)
                elif token == '*':
                    b = numb_stack.pop()
                    a = numb_stack.pop()
                    numb_stack.append(a * b)
                elif token == '/':
                    b = numb_stack.pop()
                    a = numb_stack.pop()
                    numb_stack.append(a // b)
                elif token == '.':
                    if len(numb_stack) == 1:  # 이거 한 줄 때문에!!!!!!!!!!
                        print(f'#{test_case}', *numb_stack)
                    else:
                        print(f'#{test_case} error')
            except:
                print(f'#{test_case} error')
                break
