import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx > n:
            ans += mx - n
        else:
            mx = n
    print(f'#{test_case} {ans}')