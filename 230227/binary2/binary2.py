import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = float(input())

    lst = []
    while N * 2 != (1 or 0):
        N = N * 2
        if N >= 1:
            lst.append(1)
            N = N - 1
        else:
            lst.append(0)

        if N * 2 == (1 or 0):
            lst.append(1)
            break
    print(f'#{test_case}', end=' ')
    for i in lst:
        if len(lst) >= 13:
            print('overflow', end='')
            break
        else:
            print(i, end='')
    print()


