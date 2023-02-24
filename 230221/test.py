import sys
sys.stdin = open('sample_input.txt')


def bfs(v, N):
    # 1. visited 생성
    visited = [0] * (N + 1)
    # 2. 큐 생성
    q = []
    # 3. 시작점 인큐
    q.append(v)  # 큐 생성 때 q = [v]로 한번에 해도 됨
    # 4. 시작점 인큐 표시
    visited[v] = 1

    while q:  # q가 비어있지 않으면 즉, 빌 때까지
        t = q.pop(0)  # dequeue
        print(t, end=' ')  # t에서 처리할 일 => dequeue 출력
        # t에 인접하고, 방문한 적 없는 v

        for v in adjL[t]:
            if visited[v] == 0:
                # v enqueue
                q.append(v)
                # v enqueue 되었음을 표시
                # t에서부터 인접한거니까 거리정보를 위해 => visited[t]부터 1 더 가야하니
                visited[v] = visited[t] + 1
    print()
    print(visited[1:])  # [0, 1, 2, 2, 3, 3, 4, 3] => 1 ~ 7에 대한 거리정보(4는 6의 거리정보)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V + 1)]  # 인접 리스트(V번까지 필요하니까 V + 1)

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print(adjL[1:])

bfs(1, V)  # 시작 정점 1, 마지막 정점 V