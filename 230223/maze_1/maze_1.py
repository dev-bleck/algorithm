import sys
sys.stdin = open('sample_input.txt')


def depth_first_search(y, x, maze, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited[y][x] = 1
    for direction in directions:
        new_x = direction[0] + x
        new_y = direction[1] + y
        if 0 <= new_x < 16 and 0 <= new_y < 16 \
                and maze[new_y][new_x] != 1 \
                and visited[new_y][new_x] == 0:
            if maze[new_y][new_x] == 3:
                return 1
            if depth_first_search(new_y, new_x, maze, visited) == 1:
                return 1
    return 0


for test_case in range(1, 11):
    _ = input()
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    start_i, start_j = None, None
    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                start_i, start_j = i, j
                break
        if start_i and start_j:
            break

    print(f'#{test_case} {depth_first_search(start_i, start_j, data, visited)}')
