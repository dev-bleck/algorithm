import sys
sys.stdin = open('sample_input.txt')

# work_num : 몇 번 작업까지 배정했는지
# current_prob : 현재 작업까지 진행한 뒤 전체 성공률
def work(work_num, current_prob):
    global max_prob
    # 현재 확률이 최대 확률보다 작을 때
    if current_prob <= max_prob:
        return

    # 끝까지 왔으면 최대확률이다
    if work_num == N:
        max_prob = current_prob
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            work(work_num + 1, current_prob * arr[work_num][i])
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 직원의 수, 작업의 수

    # 전처리 방법 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    # 전처리 방법 2
    # arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    # 여태까지 진행한 작업들 체크
    visited = [0 for _ in range(N)]
    max_prob = 0
    # 하나의 작업도 진행하지 않았을 때
    # 확률은 무조건 성공이다
    work(0, 1)

    print(f'#{test_case} {max_prob * 100:6f}')