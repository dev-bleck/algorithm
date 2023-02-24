import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    strings = [input() for _ in range(8)]

    cnt = 0
    for i in range(8-N+1):
        for y in range(8):
            result = ''
            for x in range(N):
                result += strings[y][x+i]
            if result == result[::-1]:
                cnt += 1

        for x in range(8):
            result = ''
            for y in range(N):
                result += strings[y+i][x]
            if result == result[::-1]:
                cnt += 1

    print(f'#{test_case} {cnt}')
