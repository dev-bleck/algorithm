# 농장의 크기는 NxN (N은 항상 홀수)
# 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    lst = []
    i = 0
    for y in range(N):
        for x in range(N // 2 - i, N // 2 + i + 1):
            lst.append(farm[y][x])
        i += 1
        if i == N // 2:
            break

    i = 0
    for y in range(N - 1, 0, -1):
        for x in range(N // 2 - i, N // 2 + i + 1):
            lst.append(farm[y][x])
        i += 1
        if i == N // 2 + 1:
            break

    print(f'#{test_case} {sum(lst)}')
