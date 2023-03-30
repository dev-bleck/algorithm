def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:  # 델타 탐색
        ni, nj = i + di, j + dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:  # 다른 퀸이 있다면
                return 0       # 실패
            ni, nj = ni + di, nj + dj

    return 1  # i, j에 퀸을 놓을 수 있음


def f(i, N):
    global cnt
    if i == N:  # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i + 1, N)  # 다음행으로
                board[i][j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f'#{test_case} {cnt}')