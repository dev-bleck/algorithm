import sys
sys.stdin = open('sample_input.txt')


def in_order(i):
    global lst
    if 0 < i <= V:
        in_order(i * 2)
        lst.append(i)
        in_order(i * 2 + 1)


T = int(input())

for test_case in range(1, T + 1):
    V = int(input())

    tree = [i for i in range(1, V + 1)]
    lst = []

    in_order(1)
    print(f'#{test_case}')
    print(f'{tree}')
    print(f'{lst}')