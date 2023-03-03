import sys

sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    strings = [list(map(str, input())) for _ in range(8)]
    result = []
    for y in range(8):
        for x in range(8 - N + 1):
            lst = []
            for i in range(N):
                lst.append(strings[y][x + i])
            result.append(lst)

    for y in range(8 - N + 1):
        for x in range(8):
            lst = []
            for i in range(N):
                lst.append(strings[y + i][x])
            result.append(lst)

    ans = 0
    for i in result:
        if i == i[::-1]:
            ans += 1

    print(f'#{test_case} {ans}')