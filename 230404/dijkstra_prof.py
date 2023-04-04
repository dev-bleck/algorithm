'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
4 3 2
3 5 1
4 5 5
'''
V, E = map(int, input().split())
max_weight = 10
# 최대 비용 + E를 기준으로 인접행렬 생성
adj_matrix = [[max_weight * E] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    start, end, weight = map(int, input().split())
    # 반대방향은 만들지 않는다
    adj_matrix[start][end] = weight


def dijkstra(max_weight = 10):
    distance = [max_weight * E] * (V + 1)
    visited = [0] * (V + 1)
    # 시작점까지 가는데 걸리는 비용은 0
    distance[0] = 0

    # 모든 정점들을 방문할 때까지
    for _ in range(V):
        min_idx = -1
        min_value = max_weight * E
        # 최솟값 점 찾기
        for i in range(V + 1):
            # 아직 방문하지 않은 점들 중
            # 방문하는데 비용이 가장 적은 점 고르기
            if not visited[i] and min_value > distance[i]:
                min_idx = i
                min_value = distance[i]
        visited[min_idx] = 1

        for i in range(V + 1):
            # distance[i]에는 여태까지 기록된 i에 도달하는 최솟값이 저장되어 있음
            # distance[min_idx] + adj_matrix[min_idx][i] : 지금 방문한 min_idx 에서 i까지 가는데 걸리는 거리와 min_idx 에 도달하는데 걸린 거리를 합한 것
            if not visited[i] and distance[i] > distance[min_idx] + adj_matrix[min_idx][i]:
                distance[i] = distance[min_idx] + adj_matrix[min_idx][i]
    # V까지 도달하는데 걸린 거리를 반환
    return distance[V]

print(dijkstra())