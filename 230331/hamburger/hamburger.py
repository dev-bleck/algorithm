import sys
sys.stdin = open('sample_input.txt')


def dfs(n, calc, score):
    if calc > L:
        return

    if n == N - 1:
        return

    dfs(n + 1, calc + lst[0][1])




T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    calc = score = 0
    dfs(0, calc, score)
    print(f'#{test_case} {lst} {score}')