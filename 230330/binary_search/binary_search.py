# left : 찾는 기준 왼쪽
# right : 찾는 기준 오른쪽
# target : 찾고 있는 목표
# direction : 마지막으로 살펴본 방향
def binary_search(left, right, target, direction):
    global answer
    middle = (left + right) // 2

    # 규칙을 어기지 않고 찾아냄
    if target == source[middle]:
        answer += 1
        return

    # target이 오른쪽에
    elif target > source[middle]:
        # 오른쪽으로 왔는데 다시 오른쪽으로 가면 실패
        if direction == 'RIGHT':
            return

        binary_search(middle + 1, right, target, 'RIGHT')

    # target이 왼쪽에
    elif target < source[middle]:
        # 왼쪽으로 왔는데 다시 왼쪽으로 가면 실패
        if direction == 'LEFT':
            return

        binary_search(left, middle - 1, target, 'LEFT')


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    source = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    answer = 0
    for target in targets:
        binary_search(0, N - 1, target, 'START')

    print(f'#{test_case} {answer}')