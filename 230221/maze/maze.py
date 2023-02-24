import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    delta_x = [0, 0, -1, 1]
    delta_y = [-1, 1, 0, 0]

    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start_x = x
                start_y = y

    visited = [[0] * N for _ in range(N)]
    visited[start_y][start_x] = 1

    queue = [(start_y, start_x)]

    while queue:
        y, x = queue.pop()

        if maze[y][x] == 3:
            print(f'#{test_case} {visited[y][x] - 2}')
            break

        for i in range(4):
            new_x = x + delta_x[i]
            new_y = y + delta_y[i]
            if (0 <= new_x < N and 0 <= new_y < N) and (visited[new_y][new_x] == 0) and (maze[new_y][new_x] != 1):
                queue.append((new_y, new_x))
                visited[new_y][new_x] = visited[y][x] + 1

    else:
        print(f'#{test_case} 0')