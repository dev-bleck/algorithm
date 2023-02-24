T = 10
# len 함수 구현
# def len(iterlable):
#     count = 0
#     for _ in iterlable:
#         count += 1
#
#     return count

# min 함수 구현
# def min(iterable):
#     min_value = 100
#     for item in iterable:
#         if item < min_value:
#             min_value = item
#
#     return min_value

# max 함수 구현
# def max(iterable):
#     max_value = 0
#     for item in iterable:
#         if item > max_value:
#             max_value = item
#
#     return max_value

# list 안에 value가 있는지를 찾아서 idx를 반환하는 함수 구현
def find_in_list(value, iterable):
    for idx in range(len(iterable)):
        if iterable[idx] == value:
            return idx

def get_max_idx(boxes):
    max_value = 0
    max_idx = -1

    for i in range(len(boxes)):
        if boxes[i] > max_value:
            max_value = boxes[i]
            max_idx = i
    return max_idx

def get_min_idx(boxes):
    min_value = 100
    min_idx = -1

    for i in range(len(boxes)):
        if boxes[i] < min_value:
            min_value = boxes[i]
            min_idx = i
    return min_idx

for test_case in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(N):
        # max_height = max(boxes) # 제일 높은 상자의 높이
        # max_idx = find_in_list(max_height, boxes) # 그 상자의 idx
        max_idx = get_max_idx(boxes)

        # min_height = min(boxes)  # 제일 낮은 상자의 높이
        # min_idx = find_in_list(min_height, boxes) # 그 상자의 idx
        min_idx = get_min_idx(boxes)

        boxes[min_idx] += 1 # 제일 높은 상자 1 감소
        boxes[max_idx] -= 1 # 제일 낮은 상자 1 증가가

    answer = max(boxes) - min(boxes)

    print(f'#{test_case} {answer}')