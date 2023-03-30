def merge_sort(numbers):
    global answer

    # 리스트에 숫자가 하나만 남은 시점
    if len(numbers) == 1:
        # 돌아가기
        return numbers

    mid = len(numbers) // 2
    left_numbers = merge_sort(numbers[:mid])
    right_numbers = merge_sort(numbers[mid:])

    left_idx = right_idx = k = 0

    # 왼쪽 또는 오른쪽 원소들 다 검증할 때까지
    while left_idx < len(left_numbers) and right_idx < len(right_numbers):
        if left_numbers[left_idx] < right_numbers[right_idx]:
            numbers[k] = left_numbers[left_idx]
            left_idx += 1
        else:
            numbers[k] = right_numbers[right_idx]
            right_idx += 1
        k += 1

    # 남은 애들도 넣어준다
    if left_idx < len(left_numbers):
        numbers[k:] = left_numbers[left_idx:]

    if right_idx < len(right_numbers):
        numbers[k:] = right_numbers[right_idx:]

    # 교수님이 정한 추가 조건
    if left_numbers[-1] > right_numbers[-1]:
        answer += 1

    return numbers


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    result = merge_sort(numbers)
    print(f'#{test_case} {result[N//2]} {answer}')