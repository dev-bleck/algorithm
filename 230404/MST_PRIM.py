"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
# heap import
import heapq

# heapq 사용 예시
# list queue가 있을 때,
# heapq.heapify(queue) : queue를 heap처럼 사용하게끔 준비
# heapq.heappush(queue, item) : queue에 item을 추가
# heapq.heappop(queue) : queue에서 가장 작은 값을 pop
# 이때 queue에서 item들 중 가중치는 item[0]
# queue = [(7, 2, 3), (4, 5, 6), (3, 5, 7)]
# heapq.heapify(queue)
# print(heapq.heappop(queue))
# print(heapq.heappop(queue))
# print(heapq.heappop(queue))

V, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]

# 인접 리스트 초기화
adj_list = [[] for _ in range(V + 1)]
for edge in arr:
    # heapq를 쓰기 때문에, 가장 앞쪽 데이터가 가중치로 판단된다
    adj_list[edge[0]].append((edge[2], edge[0], edge[1]))
    adj_list[edge[1]].append((edge[2], edge[1], edge[0]))


def mst_prim(start_node = 0):
    # 방문한 적이 있다 = 선택된 노드이다
    visited = [0 for _ in range(V + 1)]
    # 총 가중치
    total_weight = 0
    # 선택된 간선들
    result_mst = []
    # 최초로 방문하는 노드 방문 처리
    visited[start_node] = 1
    # heap으로 활용할 queue
    # 시작점의 간선 정보를 담고 시작
    queue = adj_list[start_node][:]
    # list를 heap으로 변환
    heapq.heapify(queue)

    while queue:
        # 다음 노드의 간선들을 추가하기 위해 확인
        weight, start, end = heapq.heappop(queue)
        # 방문한 적이 없는 노드라면
        if not visited[end]:
            visited[end] = 1
            total_weight += weight
            if start > end:
                result_mst.append((end, start, weight))
            else:
                result_mst.append((start, end, weight))
            # 방문한 노드의 간선 정보를 heap에 추가
            for edge in adj_list[end]:
                if not visited[edge[2]]:
                    heapq.heappush(queue, edge)

    return total_weight, result_mst

print(mst_prim())

for edge in mst_prim(start_node=6)[1]:
    print(edge)