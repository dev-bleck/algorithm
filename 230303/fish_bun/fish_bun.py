import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 정렬 필수
    lst = sorted(list(map(int, input().split())))
    cnt = 0
    ans = 'Possible'
    for t in lst:
        cnt += 1
        # 도착한 사람 수 > 만들어진 빵 수
        if cnt > (t // M) * K:
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')