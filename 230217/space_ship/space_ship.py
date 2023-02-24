import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # test_case input

# 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
delta_x = [-1, 0, 1, -1, 1, -1, 0, 1]
delta_y = [-1, -1, -1, 0, 0, 1, 1, 1]

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 크기 input
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 input
    result = 0  # 최종 결과값 : 조건(4개 이상)을 충족하는 개수

    for y in range(N):  # y좌표 반복
        for x in range(M):  # x좌표 반복
            cnt = 0  # 착륙지 높이 보다 낮은 지역 카운트
            for i in range(8):  # 델타 탐색
                new_x = x + delta_x[i]
                new_y = y + delta_y[i]
                # 배열의 범위를 벗어나지 않기 위한 조건
                if 0 <= new_x < M and 0 <= new_y < N:
                    if arr[y][x] > arr[new_y][new_x]:
                        cnt += 1  # 착륙지가 더 높으면 cnt 1 증가
            # cnt가 4 이상이면
            if cnt >= 4:
                # result 1 증가
                result += 1

    # test_case와 결과 출력
    print(f'#{test_case} {result}')
