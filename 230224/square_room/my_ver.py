import sys
sys.stdin = open('sample_input.txt')

T  = int(input())

for test_case in range(1, T + 1):
    # 상 하 좌 우
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]

    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    answer = []
    for y in range(N):
        for x in range(N):
            cnt = 1
            for i in range(4):
                new_x = x + delta_x[i]
                new_y = y + delta_y[i]
                if 0 <= new_x < N and 0 <= new_y < N and visited[new_y][new_x] == 0 and \
                    lst[new_y][new_x] - lst[y][x] == 1:
                    visited[new_y][new_x] = 1
                    cnt += 1
                    answer.append([lst[new_y][new_x], lst[y][x], cnt])

    print(f'#{test_case} {answer}')