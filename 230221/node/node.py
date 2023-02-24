import sys
sys.stdin = open('sample_input.txt')


def bfs(N, S, G):
    # visited 생성
    visited = [0] * (N + 1)
    # 큐 생성
    queue = []
    # 시작점 enqueue
    queue.append(S)  # 큐 생성 때 queue = [S]로 한번에 해도 됨
    # 4. 시작점 enqueue 표시
    visited[S] = 1

    while queue:  # queue가 빌 때까지
        t = queue.pop(0)  # dequeue

        # t에 인접하고, 방문한 적 없는 v
        for v in adjL[t]:
            if visited[v] == 0:
                # v enqueue
                queue.append(v)
                # t에서부터 인접한 거리정보 =>
                # visited[t]부터 1 더 가야하니 visited[t] + 1
                visited[v] = visited[t] + 1

    # visited[G] 또는 visited[S]가 0이라면
    # => 방문한 적이 없다
    # => 간선이 이어져 있지 않다
    if visited[G] == 0 or visited[S] == 0:
        # 0 출력
        return 0
    else:
        # 도착지와 출발지의 거리 차이 출력
        return visited[G] - visited[S]


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]  # ex) [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    adjL = [[] for _ in range(V + 1)]  # 인접 리스트 생성(V번까지 필요하니까 V + 1)
    S, G = map(int, input().split())

    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)
        # ex) [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    print(f'#{test_case} {bfs(V, S, G)}')