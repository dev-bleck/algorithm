import sys, pprint
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    edges = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = edges[i * 2], edges[i * 2 + 1]
        adj[v1][v2] = 1
    ans = []
    def bfs(start):
        stack = [start]  # 시작점은 이미 방문했으니 stack에 넣고 시작

        # stack이 empty 할 때까지 반복
        while stack:  # []는 Falsy하기 때문에
            now = stack.pop()  # pop
            # 미방문
            # 방문 순서에 따라 stack에 반복적으로 기록될 수 있어서,
            # 방문 여부를 먼저 체크해준다
            if visited[now] == 0:
                visited[now] = 1
                ans.append(now)
                # next는 다음 정점
                # V부터 1까지
                for next in range(V, 0, -1):
                    # 연결되어 있고 and 아직 방문하지 않았으면
                    if adj[now][next] == 1 and visited[next] == 0:
                        # 방문할 곳에 push(=기록)
                        stack.append(next)  # push
    bfs(edges[0])
    print(f'#{test_case}', *ans)
