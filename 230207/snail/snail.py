import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    x = y = 0
    arr[y][x] = 1 # 시작점

    # delta sort 활용
    #          우 하 좌 상
    delta_x = [1, 0, -1, 0]
    delta_y = [0, 1, 0, -1]

    dir_idx = 0  # 어느 방향으로 갈지에 대한 인덱스
    cnt = 2  # 1은 이미 넣었으니까

    while cnt <= N ** 2:  # ex) N == 3이면, 작성하는 숫자는 9까지
        new_x = x + delta_x[dir_idx]
        new_y = y + delta_y[dir_idx]

        # 다음 좌표(new_x, new_y)가 아직 사각형 안에 있는지 확인
        # + 거기에 방문한 적 없는지 확인 => 이 2가지를 충족시켜야 함
        if (0 <= new_x < N and 0 <= new_y < N) and arr[new_y][new_x] == 0:
            arr[new_y][new_x] = cnt

            x, y = new_x, new_y  # 현 위치 갱신
            cnt += 1  # 다음 쓸 숫자
        elif dir_idx == 3:  # 우하좌상 다 돌았으면
            dir_idx = 0  # 다시 우방향
        else:  # 아니면
            dir_idx += 1  # 다음 방향 (우하좌상 순서)

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()