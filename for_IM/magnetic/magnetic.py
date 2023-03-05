import sys

sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().replace(' ', '').replace('0', '') for _ in range(N)]
    arr = list(zip(*arr))
    ans = 0
    for i in arr:
        for idx in range(len(i)):
            if i[idx:idx+2] == '12':
                ans += 1

    print(f'#{test_case} {ans}')