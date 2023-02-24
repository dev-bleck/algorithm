# sample_input open
import sys
sys.stdin = open('sample_input.txt')

test_case = 10
for tc in range(1, test_case + 1):
    # 건물의 개수 N
    N = int(input())

    # N개의 건물의 높이
    height = list(map(int, input().split()))
    # 현재 가능한 세대의 수
    able_count = 0
    # 반복문의 범위 : 2번째 index부터 N - 2번째 index까지
    for idx in range(2, N - 2):
        # 현재 인덱스의 앞 2칸, 뒤 2칸을 리스트로 만들어서
        lst = [height[idx - 2], height[idx - 1], height[idx + 1], height[idx + 2]]
        # 현재 인덱스의 값에서 리스트의 최댓값을 뺏을 때 양수이면,
        if height[idx] - max(lst) > 0:
            # 그 값만큼 가능한 세대 수에 추가한다
            able_count += height[idx] - max(lst)

    # 가능한 세대 수 출력
    print(f'#{tc} {able_count}')