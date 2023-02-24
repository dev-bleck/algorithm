import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    stack = []
    for str in input():
        if (not stack and str == "}") or (not stack and str == ")"):
            stack.append(str)
            break
        elif str == "(" or str == "{":
            stack.append(str)
        elif str == ")" and stack[-1] == "(":
            stack.pop()
        elif str == "}" and stack[-1] == "{":
            stack.pop()
        # ' '안에 있는 애들 어떻게 하지?

    if stack:
        print(f'#{test_case} 0')
        print(stack)
    else:
        print(f'#{test_case} 1')
        print(stack)

