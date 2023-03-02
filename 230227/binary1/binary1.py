import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, hex = input().split()
    N = int(N)
    lst = []
    for i in hex:
        if i in 'ABCDEF':
            if i == 'A':
                i = 10
            elif i == 'B':
                i = 11
            elif i == 'C':
                i = 12
            elif i == 'D':
                i = 13
            elif i == 'E':
                i = 14
            elif i == 'F':
                i = 15
            lst.append(int(i))
        else:
            lst.append(int(i))

    result = []
    for i in lst:
        tmp = []
        while i // 2 != 0:
            tmp.append(i % 2)
            i = i // 2
        else:
            if i == 0:
                tmp.append(0)
            else:
                tmp.append(1)

        while len(tmp) < 4:
            tmp.append(0)
        result.append(tmp[::-1])

    print(f'#{test_case}', end=' ')
    for i in result:
        for j in i:
            print(j, end='')
    print()
