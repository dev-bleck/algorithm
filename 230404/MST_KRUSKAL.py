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
# x가 속한 집합의 대표 return
def findset(x):
    # x == rep[x]가 될 때까지
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    # y의 대표 원소가 x의 대표 원소를 가리키도록 함
    rep[findset(y)] = findset(x)


# V : 정점 번호 / E : 간선 수
V, E = map(int, input().split())

# makeset()
rep = [i for i in range(V + 1)]  # [0, 1, 2, 3, 4, 5, 6]
graph = []

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# [1] 가중치 기준 오름차순 정렬
graph.sort(key=lambda x: x[2])

# [2] N개 정점(V + 1)에 대해서 N - 1개의 간선 선택
N = V + 1
# s : MST에 포함된 간선의 가중치 합
s = 0
# cnt : 선택한 횟수
cnt = 0
MST = []
# 가중치가 작은 것부터
for v1, v2, w in graph:
    # 두 개의 대표 원소가 다르다 => 사이클이 생기지 않는다
    if findset(v1) != findset(v2):
        # 횟수 증가
        cnt += 1
        # 가중치 합
        s += w
        MST.append([v1, v2, w])
        # 같은 집합에 포함
        union(v1, v2)
        # 모든 선택이 끝났다면 => MST 구성이 완료되었다면
        if cnt == N - 1:
            break

print(f"최소 가중치의 합 : {s}")
print(f"선택된 정점 : {MST}")
