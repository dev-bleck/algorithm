import sys
sys.stdin = open('sample_input.txt')


def bt(row, n, now_sum, visited):
    global min_sum

    # 현재 행 == 배열의 갯수 => 마지막까지 탐색을 했을 때,
    if row == n:
        # 현재 합이 최소 합보다 작으면
        if now_sum < min_sum:
            min_sum = now_sum  # 최소 합을 현재 합으로 대체

    # 현재 합이 최소 합보다 크면
    elif now_sum > min_sum:
        # 유망하지 않음 => 더 탐색할 필요 없으니 가지치기
        return
    else:
        for col in range(n):
            if visited[col] == 0:  # 방문 안했으면
                visited[col] = 1  # 방문하기
                # 재귀
                # 다음 행 탐색, 현재까지의 합 넘겨줌, visited 갱신
                bt(row + 1, n, now_sum + numb_array[row][col], visited)
                visited[col] = 0  # 재탐색을 위해 초기화

                # Q1. visited[col] = 0의 의미와 순회 구조.
                # Q2. now_sum이 왜 계속 쌓이지 않는건지. 재귀 구조를 모르겠다.


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numb_array = []
    for _ in range(N):
        numb_array.append(list(map(int, input().split())))
    min_sum = 9 * N * N + 1  # 최소값 설정 위한 큰 수 할당
    visited = [0] * N  # 방문 여부 확인 리스트 생성

    bt(0, N, 0, visited)

    print(f'#{test_case} {min_sum}')