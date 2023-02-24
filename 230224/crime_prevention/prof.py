import sys
sys.stdin = open('sample_input.txt')


# k는 범위 크기, houses는 집들의 리스트, city_size는 N, margin은 집 당 지불 비용
def check_profit(k, houses, city_size, margin):
    # k의 크기에서 서비스 가능한 최대 집 수
    result = 0
    cost = k * k + (k - 1) * (k - 1)

    # 모든 지점에서 서비스 시도
    for i in range(city_size):
        for j in range(city_size):  # 범위 내에 집이 몇 개인지
            house_count = 0
            for house_y, house_x in houses:
                # 이 지점에서 도달 가능한 집일 때
                if abs(i - house_y) + abs(j - house_x) <= k - 1:
                    house_count += 1

            # 이득이 남고, 가장 많은 집에 서비스 가능
            profit = house_count * margin - cost
            if profit >= 0 and house_count > result:
                result = house_count

            # 상동 조건문(조금 더 느림)
            # if profit >= 0:
            #     result = max(result, house_count)

    return result

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = []  # 집들의 좌표를 저장하는 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))

    # 상동
    # houses = []
    # for i in range(N):
    #     line = list(map(int, input().split()))
    #     for j in range(N):
    #         if line[j]:
    #             houses.append((i, j))

    result = 0
    for k in range(N + 2, 0, -1):
        result = max(check_profit(k, houses, N, M), result)

    print(f'#{test_case} {result}')