import sys
sys.stdin = open('sample_input.txt')


def quick_sort(arr):
    # arr의 길이가 1보다 작거나 같으면
    if len(arr) <= 1:
        # 바로 arr을 반환
        return arr

    # 방법 1.
    # pivot : 리스트의 중간값으로 설정
    pivot = arr[len(arr) // 2]
    # pivot과 대소관계를 비교하여 담길 리스트
    left_side, equal_side, right_side = [], [], []

    for num in arr:
        if num < pivot:     # pivot보다 작으면
            left_side.append(num)
        elif num > pivot:   # pivot보다 크면
            right_side.append(num)
        else:               # pivot과 같으면
            equal_side.append(num)

    # 방법 2. (시간초과)
    pivot = arr[0]  # pivot은 첫 번째 원소
    tail = arr[1:]  # pivot을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽(pivot 보다 작은) 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽(pivot 보다 큰) 부분
    equal_side = [pivot]

    # 정렬된 왼쪽 부분 + pivot 부분 + 정렬된 오른쪽 부분
    return quick_sort(left_side) + equal_side + quick_sort(right_side)


T = int(input())

for test_case in range(1, T + 1):
    # N : 정수의 개수
    N = int(input())
    # arr : N개의 정수를 담는 리스트
    arr = list(map(int, input().split()))
    # A : N개의 정수를 정렬한 리스트
    A = quick_sort(arr)
    # 결과값 A[N // 2] 출력
    print(f'#{test_case} {A[N // 2]}')