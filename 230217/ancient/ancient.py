# 점점 커지는 당근의 가로 세로 버전?
import sys
sys.stdin = open('sample_input.txt')


def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))  # transpose

    ans = count(arr)
    t = count(arr_t)

    if ans < t:
        ans = t

    print(f'#{test_case} {ans}')