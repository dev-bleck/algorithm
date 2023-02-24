# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # K : 최대 이동 정류장 수
    # N : 종점 => 전체 정류장 수
    # M : 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # 예시에서 N = 10이면, 정류장은 0번째부터 10번째까지이므로 N += 1
    N += 1
    # 충전기가 설치된 정류장 list
    charge_station = list(map(int, input().split()))
    # 충전기가 설치된 정류장을 체크한 list
    counts = [0] * N

    # 충전기가 설치된 정류장 체크
    for i in charge_station:
        counts[i] += 1

    charge_count = 0  # 충전 횟수
    for i in range(0, N - K, K):  # 반복 범위는 0부터 N - K까지, K 단위로
        if K >= N:
            charge_count = 0
            break

        whether_charge = 0  # 범위 내에 충전소가 있는지 여부

        for j in range(1, K):  # 현재 인덱스의 다음부터 k번째까지 확인
            if counts[i + j] == 1:  # 충전소가 있으면 whether_charge는 1
                whether_charge = 1

        if whether_charge == 0:  # 충전소가 없으면 whether_charge는 0
            charge_count = 0  # 종점에 도착할 수 없는 경우 0
            break  # 반복문 탈출
        elif whether_charge == 1:  # 충전소가 있으면
            charge_count += 1  # 충전 횟수 + 1

    # 충전 횟수 출력
    print(f'#{test_case} {charge_count}')