import sys
import pprint
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]
    flag = 'NO'

    for y in range(N - 4):
        for x in range(N - 4):
                if omok[y][x] == 'o':
                    if omok[y+1][x+1] == 'o':
                        if omok[y+2][x+2] == 'o':
                            if omok[y+3][x+3] == 'o':
                                if omok[y+4][x+4] == 'o':
                                    flag = 'YES'
                                    break

    for y in range(N - 4):
        for x in range(N):
            if omok[y][x] == 'o':
                if omok[y+1][x-1] == 'o':
                    if omok[y+2][x-2] == 'o':
                        if omok[y+3][x-3] == 'o':
                            if omok[y+4][x-4] == 'o':
                                flag = 'YES'
                                break

    for y in range(N):
        count = 0
        for x in range(N):
            if omok[y][x] == 'o':
                count += 1
            else:
                count = 0
        if count == 5:
            flag = 'YES'
            break

    for x in range(N):
        count = 0
        for y in range(N):
            if omok[y][x] == 'o':
                count += 1
            else:
                count = 0
        if count == 5:
            flag = 'YES'
            break

    if flag == 'NO':
        print(f'#{test_case} NO')
    elif flag == 'YES':
        print(f'#{test_case} YES')
