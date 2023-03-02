import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N : 손님 수 / M : 만드는 시간 / K : 만든 개수
    N, M, K = map(int, input().split())
    # 일단 손님 도착 시간 순으로 정렬
    arrival = sorted(list(map(int, input().split())))
    result = 'Possible'

    bread = 0
    while True:
        bread = 1
        # 2 2
        # 2 4
        # 3 4

        # 2 2
        # 2 4
        # 1 2

        # 2 1
        #

    print(f'#{test_case} {arrival}')