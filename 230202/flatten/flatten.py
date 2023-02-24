# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = 10 # test_case

for test_case in range(1, T + 1):
    # 덤프 횟수
    dump_count = int(input())
    # 박스 높이
    box_heights = list(map(int, input().split()))

    # 덤프 횟수만큼 반복
    for _ in range(dump_count):
        # 박스 오름차순 정렬
        for i in range(0, len(box_heights) - 1):
            if box_heights[i] > box_heights[i + 1]:
                box_heights[i], box_heights[i + 1] = box_heights[i + 1], box_heights[i]
        # 최고점 - 1
        box_heights[0] += 1
        # 최저점 + 1
        box_heights[-1] -= 1

    # 최종 정렬
    for i in range(0, len(box_heights) - 1):
        if box_heights[i] > box_heights[i + 1]:
            box_heights[i], box_heights[i + 1] = box_heights[i + 1], box_heights[i]

    # 최고점과 최저점의 높이 차
    print(f'#{test_case} {box_heights[-1] - box_heights[0]}')