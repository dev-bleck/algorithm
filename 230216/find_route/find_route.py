import sys
sys.stdin = open('sample_input.txt')


def depth_first_search(now, visited):
    visited[now] = 1
    # ----- Back Tracking -----
    # 99에 가본적이 있다면 바로 멈춤
    if visited[99] == 1:
        return
    # -------------------------

    for next in range(100):
        # 연결 되어있고 and 방문한적 없다면
        if connections[now][next] == 1 and visited[next] == 0:
            depth_first_search(next, visited)


for _ in range(10):
    test_case, edges = map(int, input().split())
    raw_data = list(map(int, input().split()))

    # 0 ~ 99
    visited = [0 for _ in range(100)]

    connections = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(edges):
        # 간선 정보 입력
        connections[raw_data[i * 2]][raw_data[i * 2 + 1]] = 1

    depth_first_search(0, visited)
    # visited 업데이트 하면서 도착 정보 확인하기
    print(f'#{test_case} {visited[99]}')
