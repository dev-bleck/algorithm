import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    # y의 대표 원소가 x의 대표 원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                        # N : 섬의 개수
    x = list(map(int, input().split()))     # x : 섬들의 x좌표
    y = list(map(int, input().split()))     # y : 섬들의 y좌표
    E = float(input())                      # E : 환경 부담 세율

    arr = [[0, 0]]                          # arr : 섬 별 좌표를 저장할 리스트
    for i in range(N):
        arr.append([x[i], y[i]])

    rep = [i for i in range(N + 1)]         # rep : 대표값 저장 리스트
    graph = []

    # 첫번째 섬과 두번째 섬의 좌표 비교
    for island_1 in range(1, N + 1):
        for island_2 in range(island_1 + 1, N + 1):
            cost = 0
            # 첫번째 섬과 두번째 섬의 x 좌표가 같으면
            if arr[island_1][0] == arr[island_2][0]:
                # y 좌표의 차이만 비용에 반영
                cost = abs(arr[island_1][1] - arr[island_2][1])
            # 첫번째 섬과 두번째 섬의 y 좌표가 같으면
            elif arr[island_1][1] == arr[island_2][1]:
                # x 좌표의 차이만 비용에 반영
                cost = abs(arr[island_1][0] - arr[island_2][0])
            else:
                # 두 좌표 모두 다르면 계산
                cost = ((abs(arr[island_1][0] - arr[island_2][0])) ** 2 + (abs(arr[island_1][1] - arr[island_2][1])) ** 2) ** (1/2)

            # graph 리스트에 u, v, cost 추가
            graph.append([island_1, island_2, cost])

    # [1] lambda 사용 가중치 기준으로 정렬
    graph.sort(key=lambda x: x[2])

    # [2] N개 정점(V + 1)에 대해서 N - 1개의 간선 선택
    s = 0       # s : MST에 포함된 간선의 가중치 합
    cnt = 0     # cnt : 선택한 횟수
    MST = []
    # 가중치가 작은 것부터
    for u, v, weight in graph:
        # 두 개의 대표 원소가 다르다 => 사이클이 생기지 않는다
        if find_set(u) != find_set(v):
            # 횟수 증가
            cnt += 1
            # 가중치 합
            s += (weight ** 2) * E
            MST.append([u, v, weight])
            # 같은 집합에 포함
            union(u, v)
            # 모든 선택이 끝났다면 => MST 구성이 완료되었다면
            if cnt == N - 1:
                break

    # 결과 출력
    print(f'#{test_case} {round(s)}')