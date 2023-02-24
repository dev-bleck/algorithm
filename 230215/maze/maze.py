import sys
sys.stdin = open('sample_input.txt')

# 방향 판별용 상수
DIRECTIONS = [
    (-1, 0), (0, -1), (1, 0), (0, 1)
]


def find_route(maze, current):
    # for idx, direction in enumerate(DIRECTIONS):
    for idx in range(4):
        direction = DIRECTIONS[idx]

        next_point = current[0] + direction[1], current[1] + direction[0]

        # 다음에 갈 곳이 3이면 도착
        if maze[next_point[0]][next_point[1]] == 3:
            return True
        # 갈 곳이 열려있다
        elif maze[next_point[0]][next_point[1]] == 0:
            maze[next_point[0]][next_point[1]] = 1  # visited
            # 막다른 길이면
            if not find_route(maze, next_point):
                # 돌아오자
                maze[next_point[0]][next_point[1]] = 0
            # 앞서 호출한 재귀함수가 성공했다
            else:
                return True

    # 사방을 확인했지만 길이 없다
    return False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # start
    start = None
    # 범위판별이 귀찮으니 1로 감싸줌
    # 첫줄
    maze = [[1 for _ in range(N + 2)]]
    for i in range(N):
        # 왼쪽 1 추가
        maze_row = [1, ]
        # 중간 값들
        maze_row.extend(list(map(int, input())))
        # 오른쪽 1 추가
        maze_row.append(1)

        # 시작점 찾기
        for idx, value in enumerate(maze_row):
            if value == 2:
                start = (i + 1, idx)
                break

        # maze에 maze줄 추가 => 만든 줄 추가
        maze.append(maze_row)

    # 마지막 줄 1 추가
    maze.append([1 for _ in range(N + 2)])

    current = start
    # movement_stack = []
    # 마지막으로 가기 위한 변수인데 안썼음..
    # last_dir = -1

    print(f'#{test_case} {int(find_route(maze, current))}')