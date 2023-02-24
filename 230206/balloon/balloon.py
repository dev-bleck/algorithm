import sys
sys.stdin = open('sample_input.txt')

T = int(input())

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_shot = 0
    for y in range(N):
        for x in range(M):
            shot = 0
            for dir in range(5):
                fx = x + dx[dir]
                fy = y + dy[dir]
                if 0 <= fy <= N - 1 and 0 <= fx <= M - 1:
                    shot += arr[fy][fx]
            if shot > total_shot:
                total_shot = shot

    print(f'#{test_case} {total_shot}')