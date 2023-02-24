import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_len = 2

    for y in range(N):
        cnt = 0
        for x in range(M):
            if data[y][x] == 1:
                cnt += 1
                if cnt > max_len:
                    max_len = cnt
            else:
                cnt = 0

    for x in range(M):
        cnt = 0
        for y in range(N):
            if data[y][x] == 1:
                cnt += 1
                if cnt > max_len:
                    max_len = cnt
            else:
                cnt = 0

    print(f'#{test_case} {max_len}')