import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N
    selected = [-1 for _ in range(N)]  # = [-1] * N
    stack = []  # N = 3  =>  stack = [(0, 2), (0, 1), (0, 0)] => 0번줄의 2번째 칸을 선택했을 때, 0번줄의 1번째 칸을 선택했을 때, 0번줄의 0번째 칸을 선택했을 때,
    # 첫 줄을 먼저 다 스택에 넣는다
    for i in range(N - 1, -1, -1):
        stack.append((0, i))  # (row, index)

    # DFS start
    while stack:
        # 현재 검증하는 줄, 칸
        row, idx = stack.pop()  # (0, 0), (0, 1), (0, 2) 순서대로 pop
        # 현재 줄 이후는 모두 -1 처리
        for i in range(row, N):
            selected[i] = -1  # selected 초기화
        # 현재 줄의 몇번째 칸인지 기록
        selected[row] = idx

        # 부분합 구해보기
        tmp_sum = 0
        for i in range(row + 1):
            tmp_sum += arr[i][selected[i]]

        # 만약 지금까지 합이 더 크면
        if tmp_sum > min_sum:
            continue

        row += 1
        # 마지막 줄까지 확인했다면
        if row == N:
            # 결과 검증하고, 다음 것 확인
            min_sum = min(min_sum, tmp_sum)
            continue  # 아래 for문 실행하지 않고 위로 돌아감

        # 다음 줄 등록
        for i in range(N - 1, -1, -1):
            if i not in selected:
                stack.append((row, i))

    print(f'#{test_case} {min_sum}')
