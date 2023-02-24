import sys
sys.stdin = open('sample_input.txt')

T = int(input())


# 1은 가위, 2는 바위, 3은 보자기
def battle(data, left, right):
    # 나머지 연산 기준으로 승부를 가릴 수 있다
    result = (data[left] - data[right]) % 3  # 3으로 나눈 나머지 값 => 유용
    if result == 2:
        return right
    else:
        return left


# data 전체 카드들 / left : 왼쪽 인덱스(0) / right : 오른쪽 인덱스(N-1)
def separate(data, left, right):
    if left == right:
        return left

    mid = (left + right) // 2  # 중앙

    left_group = separate(data, left, mid)
    right_group = separate(data, mid + 1, right)
    return battle(data, left_group, right_group)

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    result = separate(data, 0, N - 1)

    print(f'#{test_case} {result + 1}')  # 문제에서는 시작이 1이여서 + 1