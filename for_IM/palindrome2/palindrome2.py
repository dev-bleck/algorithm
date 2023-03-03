import sys

sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1):
    N = int(input())
    strings = [list(map(str, input())) for _ in range(100)]
    result = []
    for y in range(100):
        lst = []
        for x in range(100):
            lst.append(strings[y][0:x])
        result.append(lst)

    ans = 0
    max_len = 0
    for i in range(100):
        for j in range(100):
            if result[i][j] == result[i][j][::-1]:
                ans += 1
    # print(result[0][1], result[0][1][::-1])
    # for y in range(100 - N + 1):
    #     for x in range(100):
    #         lst = []
    #         for i in range(N):
    #             lst.append(strings[y + i][x])
    #         result.append(lst)
    #
    # ans = 0
    # for i in result:
    #     if i == i[::-1]:
    #         ans += 1
    #
    print(f'#{test_case} {ans}')