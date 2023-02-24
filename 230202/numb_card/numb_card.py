# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test case count input
test_case = int(input())
# 1 ~ test case 반복
for tc in range(1, test_case + 1):
    # 카드 장수 input
    N = int(input())
    # N개의 숫자 input
    numbs = list(map(int, input()))
    # 각 숫자별 카운트를 담을 리스트
    counts = [0] * 10
    # 현재 최대값
    now_max = 0
    # 현재 최대값의 인덱스
    max_idx = 0
    
    # N개의 숫자를 세서 각각 카운트를 증가시킴
    for i in numbs:
        counts[i] += 1

    # 카운트를 담은 리스트의 길이를 범위로 인덱싱
    for idx in range(len(counts)):
        # 인덱싱한 카운트 리스트의 값이 현재 최대값보다 크거나 같으면
        if counts[idx] >= now_max:
            # 현재 최대값은 인덱싱한 카운트 리스트의 값을 할당
            now_max = counts[idx]
            # 현재 최대값의 인덱스는 현재 인덱스로 할당
            max_idx = idx

    # 결과 출력
    print(f'#{tc} {max_idx} {now_max}')