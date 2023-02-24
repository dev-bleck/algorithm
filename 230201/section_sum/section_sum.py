# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test_case count
test_case = int(input())
# test_case count만큼 반복
for tc in range(1, test_case + 1):
    # N : 정수 개수 / M : 이웃한 개수
    N, M = map(int, input().split())
    # 입력받은 정수 배열 list
    lst = list(map(int, input().split()))

    # 현재 정수 배열의 합계 최댓값
    now_sum_max = 0
    # 현재 정수 배열의 합계 최솟값
    now_sum_min = sum(lst) # 기준을 현재 배열의 총합으로 설정

    # 반복문 범위 : 정수의 개수 - 이웃한 개수 + 1
    for i in range(N - M + 1):
        # 현재 합계
        now_sum = 0
        # 이웃한 개수만큼 반복
        for j in range(M):
            # 현재 합계에 현재의 리스트의 인덱스 값을 더함
            now_sum += lst[i+j]

        # 현재 합계가 합계 최댓값 보다 크면
        if now_sum > now_sum_max:
            # 합계 최댓값에 현재 합계를 할당
            now_sum_max = now_sum
        # 현재 합계가 합계 최댓값 보다 작으면
        if now_sum < now_sum_min:
            # 합계 최솟값에 현재 합계를 할당
            now_sum_min = now_sum

    # 합계 최댓값에서 합계 최솟값을 뺀 결과 출력
    print(f'#{tc} {now_sum_max - now_sum_min}')