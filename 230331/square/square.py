import sys
sys.stdin = open('sample_input.txt')


def bfs(si, sj):
    ans = []
    q = [(si, sj)]
    v[si][sj] = 1
    ans.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 4방향 범위내, 미방문, 1 차이 나는 위치면
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and (abs(arr[ci][cj] - arr[ni][nj]) == 1):
                q = [(ni, nj)]  # q 갱신
                v[ni][nj] = 1   # visited 처리
                ans.append((arr[ni][nj]))

    # 제일 작은 번호, 길이 return
    return min(ans), len(ans)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited
    v = [[0] * N for _ in range(N)]
    # 최소값, 최소 길이 설정
    min_ans, len_ans = N * N, 0

    for i in range(N):
        for j in range(N):
            # 방문 안했다면
            if v[i][j] == 0:
                # bfs 결과 => 최소값 ,최소 길이 임시 저장
                min_tmp, len_tmp = bfs(i, j)
                # 길이가 임시 저장이 더 길거나, 길이는 같은데 번호의 크기가 임시저장이 더 작으면
                if len_ans < len_tmp or (len_ans == len_tmp and min_ans > min_tmp):
                    # 값 갱신
                    min_ans, len_ans = min_tmp, len_tmp

    print(f'#{test_case} {min_ans} {len_ans}')