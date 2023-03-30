import sys
sys.stdin = open('sample_input.txt')

def dfs(n, sm):
    global ans

    # 가지치기
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if j not in v:
            v.append(j)
            dfs(n + 1, sm + arr[n][j])
            v.pop()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 100 * N
    v = []
    dfs(0, 0)
    print(f'#{test_case} {ans}')