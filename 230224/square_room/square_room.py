import sys
sys.stdin = open('sample_input.txt')


def bfs(si, sj):
    # [2] q 생성, v 입력(은 이미 함), alst 생성
    q = []
    alst = []
    # [3] 초기 데이터 삽입
    q.append((si, sj))
    # [4] visited 배열 표시
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)

        # 4방향, 미방문, 조건(1차이) 맞으면,
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and \
                abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])
    return min(alst), len(alst)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [1] visited 생성, 함수 호출,
    v = [[0] * N for _ in range(N)]
    ans, cnt, = N * N, 0
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                # 최대인 방이 여럿이라면 적힌 수가 가장 작은것
                if cnt < tcnt or cnt == tcnt and ans > t:
                    ans, cnt = t, tcnt

    print(f'#{test_case} {ans} {cnt}')