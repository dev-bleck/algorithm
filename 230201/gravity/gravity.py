# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test case count input
test_case = int(input())
# 1 ~ test case 반복
for tc in range(1, test_case + 1):
    # 가로 길이 N input
    N = int(input())

    # 입력받은 상자들을 split하고 정수형으로 변환하여 list로 만듬
    boxes = list(map(int, input().split()))

    # 최댓값을 저장하기 위한 변수
    max_drop = 0 # 최댓값의 최솟값은 상자들이 하나도 움직이지 않을 때니까 0

    # 마지막 상자를 제외하고 확인 => N - 1
    for idx in range(N - 1):
        # 현재 상자의 높이
        box_height = boxes[idx]

        # 현재 상자보다 낮은 애들 세는 변수(떨어지는 횟수)
        tmp_drop = 0

        # 현재 상자보다 오른쪽 확인
        for j in range(idx + 1, N): # 나(idx) 다음부터 N 직전까지
            # 현재보다 작으면 +1
            if box_height > boxes[j]:
                tmp_drop += 1 # 나보다 작은 것들의 개수

        # 최댓값보다 현재 낙차가 더 크면
        if max_drop < tmp_drop:
            # 최댓값에 현재 낙차 할당
            max_drop = tmp_drop

    # 최댓값 출력
    print(f'#{tc} {max_drop}')