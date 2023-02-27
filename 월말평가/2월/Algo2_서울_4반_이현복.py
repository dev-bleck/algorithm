T = int(input())  # test_case input

for test_case in range(1, T + 1):
    # N : 하늘의 크기 / K : 영역의 크기
    # A : 초점의 Y 좌표 / B : 초점의 X 좌표
    N, K, A, B = map(int, input().split())
    sky = []  # 빈 하늘과 별 input
    for _ in range(N):
        sky.append(input().split())

    i = 0  # 최종 확대 횟수
    zoom_count = N - K + i  # range 계산을 위한 범위 + 확대 횟수
    sum_count = 0  # 현재 별의 합계
    for y in range(zoom_count, K):
        for x in range(zoom_count, K):
            if sky[y][x] == '*':
                sum_count += 1

    count = sum_count  # count : 확대해 나갈 때 현재 별의 합계
    # count와 sum_count가 같을 동안만 반복
    while sum_count == count:
        zoom_count = N - K + i
        count = 0
        for y in range(zoom_count, K):
            for x in range(zoom_count, K):
                # 해당 좌표의 값이 *인 경우 1 증가
                if sky[y][x] == '*':
                    count += 1

        # count와 sum_count가 같으면 확대 => i에 1 증가
        if sum_count == count:
            i += 1
        # 아니면 i에 1 감소
        else:
            i -= 1

    print(f'#{test_case} {i}')
