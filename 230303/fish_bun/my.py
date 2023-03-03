import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N : 손님 수 / M : 소요 시간 / K : 붕어빵 개수
    N, M, K = map(int, input().split())
    # 손님 리스트 정렬
    lst = sorted(list(map(int, input().split())))
    ans = 'Possible'

    # 붕어빵 수요
    count = 0

    for t in lst:
        # 손님이 오면 붕어빵 수요 1 증가
        count += 1
        # 붕어빵 만드는게 수요를 못 따라가면
        if count > (t // M) * K:
            # 실패
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')