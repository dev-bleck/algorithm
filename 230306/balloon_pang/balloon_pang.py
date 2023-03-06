import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    delta_x = [0, 0, -1, 1]
    delta_y = [-1, 1, 0, 0]

    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for y in range(N):
        for x in range(M):
            now_sum = balloons[y][x]
            for i in range(4):
                for j in range(1, balloons[y][x] + 1):
                    new_x = x + delta_x[i] * j
                    new_y = y + delta_y[i] * j
                    if 0 <= new_x < M and 0 <= new_y < N:
                        now_sum += balloons[new_y][new_x]
                if max_sum < now_sum:
                    max_sum = now_sum

    print(f'#{test_case} {max_sum}')