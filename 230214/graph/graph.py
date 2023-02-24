import sys
sys.stdin = open('sample_input.txt')


# baseline
def depth_first_search(start):
    stack = [start]  # 시작점 넣고 시작

    while stack:  # stack이 empty 할 때까지 반복
        now = stack.pop()

        if visited[now] == 0:  # 방문 여부 체크
            visited[now] = 1

            for next in range(V, 0, -1):
                if adjM[now][next] == 1 and visited[next] == 0:
                    stack.append(next)

    return visited  # 방문 여부 체크 리스트 반환


T = int(input())  # test case input

for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 정점, 간선 개수 input
    adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 여부 2차원 배열. 데이터는 1부터.

    adj_data = []  # 인접정보(간선)를 담기 위한 리스트
    for _ in range(E):  # 간선의 개수만큼 반복
        s, g = map(int, input().split())
        adj_data.append(s)  # 출발 노드 정보
        adj_data.append(g)  # 도착 노드 정보
    # ex) #1 adj_data = [1, 4, 1, 3, 2, 3, 2, 5, 4, 6]

    for i in range(E):  # 간선의 개수만큼 반복
        n1, n2 = adj_data[i * 2], adj_data[i * 2 + 1]
        # ex) #1 1, 4 / 1, 3 / 2, 3 / 2, 5 / 4, 6
        adjM[n1][n2] = 1
        # adjM[n2][n1] = 1
        # 위 코드를 추가하면 단방향이 아닌 양방향
        # 즉, 문제 의도대로면 단방향으로 가고 끝인데,
        # 되돌아가면서 원래는 갈 수 없는 정점까지 가게 됨

    visited = [0 for _ in range(V + 1)]  # 방문한 정점 체크

    S, G = map(int, input().split())  # 출발 노드, 도착 노드

    # 함수의 return 값이 visited
    if depth_first_search(S)[G]:  # visited에 대한 G번째 인덱스가 0이 아니면 성공
        print(f'#{test_case} 1')
    else:  # visited에 대한 G번째 인덱스가 0이면 실패
        print(f'#{test_case} 0')
