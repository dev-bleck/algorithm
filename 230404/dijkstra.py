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


# s : 출발 / V : 마지막 정점 번호
def dijkstra(s, V):
    # U : 최소비용이 결정된 정점 집합
    # visited 형식으로 생성
    U = [0] * (V + 1)
    # U = {s}에 해당하는 표현
    U[s] = 1
    # s에서 정점 i로 가는 비용
    for i in range(V + 1):
        D[i] = adjM[s][i]

    N = V + 1  # N개의 정점
    # 남은 정점의 비용 결정 => N - 1개 정점의 비용을 결정
    for _ in range(N - 1):
        # D[w]가 최소인 w를 결정
        # minV : 최솟값
        minV = INF
        w = 0
        for i in range(V + 1):
            # 남은 정점 i 중
            # U[i]가 0이면서(비용이 확정되지 않음),
            # D[i]가 최솟값이면
            if U[i] == 0 and minV > D[w]:
                w = i
                minV = D[i]

        # 최소인 w는 최소 비용 D[w] 확정
        U[w] = 1
        # w에 인접인 정점에 대해 기존 비용과 w를 거쳐가는 비용을 비교
        for v in range(V + 1):
            # w에 인접인 v의 조건
            # 인접인지를 확인(0은 자기 자신이니까 0보다 크고 INF 보다 작다면 인접)
            if 0 < adjM[w][v] < INF:
                # 기존 비용(D[v])와 w를 거쳐 가는 비용(D[w] + adjM[w][v]) 중 작은 것을 택
                D[v] = min(D[v], D[w] + adjM[w][v])


# 임의의 최대 비용 - 문제에 따라 조절
INF = 10000
# V : 0 ~ V번 정점 / E : 간선 수
V, E = map(int, input().split())
# 인접 행렬
adjM = [[INF] * (V + 1) for _ in range(V + 1)]
# 대각선(자기자신으로 가는 비용)은 0으로
for i in range(V + 1):
    adjM[i][i] = 0
for _ in range(E):
    # u에서 v로 가는 비용(가중치) w
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0] * (V + 1)
dijkstra(0, V)
# 각 정점까지 가는 최소 비용 출력
print(D)
