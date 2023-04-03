"""
# 정점의 갯수, 간선의 갯수  # 인접 연결 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(start):
    # 인접 행렬과 노드의 갯수
    global adj_matrix, V
    # DFS를 위한 스택 초기화
    stack = [start]

    # 방문여부 기록 리스트
    visited = [0 for _ in range(V + 1)]

    # 스택이 빌 때까지 반복
    while stack:
        current = stack.pop()  # 이번에 방문할 곳
        if not visited[current]:  # 방문했는지 확인
            visited[current] = 1  # 방문 체크
            print(f'방문점: {current}')

            # for node in range(V, 0, -1):  # 숫자가 작은 노드부터 다음 방문 가능한 곳 스택에 기록
            for node in range(1, V + 1):  # 숫자가 큰 노드부터 다음 방문 가능한 곳 스택에 기록
                # 현재 위치와 다음 위치가 연결되어 있고, 방문한 적이 없으면
                if adj_matrix[current][node] == 1 and visited[node] == 0:
                    stack.append(node)


def bfs(start):
    # 인접 행렬과 노드의 갯수
    global adj_matrix, V
    # BFS를 위한 큐 초기화
    queue = [start]

    # 방문여부 기록 리스트
    visited = [0 for _ in range(V + 1)]

    # 큐가 빌 때까지 반복
    while queue:
        current = queue.pop(0)  # 이번에 방문할 곳
        if not visited[current]:  # 방문했는지 확인
            visited[current] = 1  # 방문 체크
            print(f'방문점: {current}')

            # for node in range(V, 0, -1):  # 숫자가 작은 노드부터 다음 방문 가능한 곳 큐에 기록
            for node in range(1, V + 1):  # 숫자가 큰 노드부터 다음 방문 가능한 곳 큐에 기록
                # 현재 위치와 다음 위치가 연결되어 있고, 방문한 적이 없으면
                if adj_matrix[current][node] == 1 and visited[node] == 0:
                    queue.append(node)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    # i * 2와 i * 2 + 1이 연결되어 있다
    adj_matrix[arr[i * 2]][arr[i * 2 + 1]] = 1
    # 방향성이 없으니 반대방향도 해주어야 한다
    adj_matrix[arr[i * 2 + 1]][arr[i * 2]] = 1

dfs(1)
bfs(1)