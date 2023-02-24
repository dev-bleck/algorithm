import sys
sys.stdin = open('sample_input.txt')

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    # 조망권 확보된 집
    results = 0

    for idx in range(N):
        # 현재 건물의 높이
        cur_height = buildings[idx]
        # 건물의 높이가 없으면(값이 0이면)
        if not cur_height:
            continue

        max_height = 0  # 좌우 최대높이 저장 변수
        for side in range(4):  # 4번 비교
            side_idx = [-2, -1, 1, 2]  # 앞의 두 개, 뒤의 두 개
            side_height = buildings[side_idx[side] + idx]  # 현재 비교 대상 높이
            if side_height > max_height:  # 최대값 저장
                max_height = side_height

        if max_height < cur_height:  # 주변에서 내가 제일 클 때
            results += cur_height - max_height # 얼마나 큰지를 결과에 더함

    print(f'#{test_case} {results}')