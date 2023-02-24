import sys
sys.stdin = open('sample_input.txt')


def bfs(s):
    # [2] q, v, 필요한 flag 생성
    q = []
    v = [0] * 101
    ans = s  # 정답에 시작값을 넣어줘서 초기화

    # [3] q에 초기데이터(들) 삽입, v 표시
    q.append(s)
    v[s] = 1

    while q:
        # [4] q에서 한개 꺼냄
        c = q.pop(0)
        # + 필요시 정답 처리
        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c  # 조건 충족하면 정답 갱신

        # [5] 4 or 8 or 연결방향 등 조건에 따라 반복처리
        for n in adj[c]:
            if v[n] == 0:  # 미방문이면
                q.append(n)
                v[n] = v[c] + 1  # 거리 계산
    return ans


T = 10

for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] 인접 리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for idx in range(0, len(lst), 2):
        # start, end
        s, e = lst[idx], lst[idx+1]
        # 인접행렬의 start(시작 위치)에 end를 append
        adj[s].append(e)

    ans = bfs(S)  # 여기까지 만들고 위로 올라가서 함수 만들기
    print(f'#{test_case} {ans}')