import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    m = N // 2

    # 방법 1 : 규칙성
    ans = 0
    for x in range(N):
        for y in range(abs(m - x), N - abs(m - x)):
            ans += arr[x][y]

    # 방법 2 : 범위
    ans = 0
    start = end = m
    for i in range(N):
        for j in range(start, end + 1):
            ans += arr[i][j]
        # start, end 재조정
        if i < m:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{test_case} {ans}')