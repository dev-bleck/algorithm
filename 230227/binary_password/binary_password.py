import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    dict = {'0001101' : 0,
            '0011001' : 1,
            '0010011' : 2,
            '0111101' : 3,
            '0100011' : 4,
            '0110001' : 5,
            '0101111' : 6,
            '0111011' : 7,
            '0110111' : 8,
            '0001011' : 9}

    result = []
    for i in arr:
        for j in range(0, M-7, 7):
            tmp = ''
            for k in range(7):
                tmp += i[j+k]
            result.append(tmp)

    lst = []
    for i in result:
        if i != '0000000':
            lst.append(i)

    lst = lst[:7]

    # result = []
    # for i in lst:
    #     result.append(dict[i])

    print(f'#{test_case} {lst}')

