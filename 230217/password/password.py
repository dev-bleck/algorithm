import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    length, pw = map(str, input().split())
    numb_list = []

    for numb in pw:
        if not numb_list:
            numb_list.append(numb)
        elif numb_list[-1] == numb:
            numb_list.pop()
        else:
            numb_list.append(numb)

    result = "".join(numb_list)

    print(f'#{test_case} {result}')