# V = Vertice = 정점
# E = Edge = 간선
V, E = map(int, input().split())

# 인접 정보 리스트
# index 0의 아이템 => [0에 인접한 점의 인덱스]
adjL = []

# 인접 정보 2차원 리스트
# index 0의 아이템 => [1 if 인접 else 0 for i in range(V)]
adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 항상 데이터가 1부터여서 + 1..

# 인접 정보 => 간선의 수만큼 반복
adj_data = list(map(int, input().split()))

for i in range(E):
    n1, n2 = adj_data[i * 2], adj_data[i * 2 + 1]  # 서로 연결되어 있다
    adjM[n1][n2] = 1  # 연결되어 있으니 1로 업데이트
    adjM[n2][n1] = 1  # 연결되어 있으니 1로 업데이트

# '정점을 방문한적 있는지'에 대한 정보
# visited[i] == 1이면, i에 방문한 적 있음을 기록하는 리스트
visited = [0 for _ in range(V + 1)]


# start는 시작점
def depth_first_search(start):
    stack = [start]  # 시작점은 이미 방문했으니 stack에 넣고 시작

    # stack이 empty 할 때까지 반복
    while stack:  # []는 Falsy하기 때문에
        now = stack.pop()  # pop

        # 미방문
        # 방문 순서에 따라 stack에 반복적으로 기록될 수 있어서,
        # 방문 여부를 먼저 체크해준다
        if visited[now] == 0:
            visited[now] = 1
            # print(now, end='-')
            # next는 다음 정점
            # V부터 1까지
            for next in range(V, 0, -1):
                # 연결되어 있고 and 아직 방문하지 않았으면
                if adjM[now][next] == 1 and visited[next] == 0:
                    # 방문할 곳에 push(=기록)
                    stack.append(next)  # push

# 재귀함수 이용
def depth_first_search2(ver):
    # 함수 호출 되면 거기 방문한 것
    visited[ver] = 1
    print(ver, end='-')
    # 작은 숫자부터 카운트
    for next in range(1, V + 1):
        # 인접하고 and 미방문이면
        if adjM[ver][next] == 1 and visited[next] == 0:
            # 다음 함수 호출
            depth_first_search2(next)

# depth_first_search(1)
depth_first_search2(1)