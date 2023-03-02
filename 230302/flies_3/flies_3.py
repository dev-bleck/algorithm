import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_kill_count = 0

    # 상하좌우
    delta_x_1 = [0, 0, -1, 1]
    delta_y_1 = [-1, 1, 0, 0]
    for y in range(N):
        for x in range(N):
            kill_count1 = flies[y][x]
            for i in range(4):
                for j in range(1, M):
                    new_x = x + delta_x_1[i] * j
                    new_y = y + delta_y_1[i] * j
                    if 0 <= new_x < N and 0 <= new_y < N:
                        kill_count1 += flies[new_y][new_x]
            if kill_count1 > max_kill_count:
                max_kill_count = kill_count1

    # 좌상 우상 좌하 우하
    delta_x_2 = [-1, 1, -1, 1]
    delta_y_2 = [-1, -1, 1, 1]
    for y in range(N):
        for x in range(N):
            kill_count2 = flies[y][x]
            for i in range(4):
                for j in range(1, M):
                    new_x = x + delta_x_2[i] * j
                    new_y = y + delta_y_2[i] * j
                    if 0 <= new_x < N and 0 <= new_y < N:
                        kill_count2 += flies[new_y][new_x]
            if kill_count2 > max_kill_count:
                max_kill_count = kill_count2

    print(f'#{test_case} {max_kill_count}')