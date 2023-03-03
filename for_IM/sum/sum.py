import sys

sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0

    for y in range(100):
        now_sum = 0
        for x in range(100):
            now_sum += arr[y][x]
        if now_sum > ans:
            ans = now_sum

    for x in range(100):
        now_sum = 0
        for y in range(100):
            now_sum += arr[y][x]
        if now_sum > ans:
            ans = now_sum

    now_sum = 0
    for i in range(100):
        now_sum += arr[i][i]
    if now_sum > ans:
        ans = now_sum

    now_sum = 0
    for i in range(99, -1, -1):
        now_sum += arr[i][i]
    if now_sum > ans:
        ans = now_sum

    print(f'#{test_case} {ans}')