import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]

    result = 'NO'

    # 가로
    for y in range(N):
        for x in range(N - 4):
            if omok[y][x] == 'o':
                if (omok[y][x + 1] == 'o') and (omok[y][x + 2] == 'o') and (omok[y][x + 3] == 'o') and (omok[y][x + 4] == 'o'):
                    result = 'YES'
    # 세로
    for y in range(N - 4):
        for x in range(N):
            if omok[y][x] == 'o':
                if (omok[y + 1][x] == 'o') and (omok[y + 2][x] == 'o') and (omok[y + 3][x] == 'o') and (omok[y + 4][x] == 'o'):
                    result = 'YES'

    # 좌상우하
    for y in range(N - 4):
        for x in range(N - 4):
            if omok[y][x] == 'o':
                if (omok[y + 1][x + 1] == 'o') and (omok[y + 2][x + 2] == 'o') and (omok[y + 3][x + 3] == 'o') and (omok[y + 4][x + 4] == 'o'):
                    result = 'YES'

    # 우상좌하
    for y in range(N - 4):
        for x in range(N):
            if x >= 4 and omok[y][x] == 'o':
                if (omok[y + 1][x - 1] == 'o') and (omok[y + 2][x - 2] == 'o') and (omok[y + 3][x - 3] == 'o') and (omok[y + 4][x - 4] == 'o'):
                    result = 'YES'

    print(f'#{test_case} {result}')