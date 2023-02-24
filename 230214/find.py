import sys
sys.stdin = open('sample_input.txt')


def dfs(s):
    visited = [0] * 100
    stack = []

    i = s
    visited[i] = 1

    while True:
        if i == 99:
            return 1
        for w in range(100):
            if adj[i][w] == 1 and visited[w] == 0:
                visited[w] = 1
                stack.append(i)
                i = w
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return 0


T = 10
for test_case in range(1, T + 1):
    _, e = map(int, input().split())
    edges = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(100)]

    for i in range(e):
        adj[edges[i * 2]][edges[i * 2 + 1]] = 1

    print(f'#{test_case} {dfs(0)}')