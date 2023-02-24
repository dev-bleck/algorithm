# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test case count input
test_case = int(input())
# 1 ~ test case 반복
for tc in range(1, test_case + 1):
    # 양수의 개수 N input
    N = int(input())
    # 입력 받은 양수를 공백 기준으로 split 하고,
    # map을 이용해서 정수형으로 변환하고 list로 만듬
    lst = list(map(int, input().split()))

    # 현재 최댓값, 현재 최솟값은 list의 0번째
    now_max, now_min = lst[0], lst[0]

    # 양수의 개수만큼 반복
    for idx in range(N):
        # 현재 최댓값보다 리스트의 idx번째 값이 더 크면
        if now_max < lst[idx]:
            # 현재 최댓값을 리스트의 idx번째 값으로 변경
            now_max = lst[idx]
        # 현재 최솟값보다 리스트의 idx번째 값이 더 크면
        elif now_min > lst[idx]:
            # 현재 최솟값을 리스트의 idx번째 값으로 변경
            now_min = lst[idx]

    # 가장 큰 수와 가장 작은 수의 차이 출력
    print(f'#{tc} {now_max - now_min}')