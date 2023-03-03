import sys
sys.stdin = open('sample_input.txt')

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(zip(*arr))
    ans = 0

    for lst in arr_t:
        prev = '0'
        for n in lst:
            if n != '0':
                if n == '2' and prev == '1':
                    ans += 1
                prev = n

    print(f'#{test_case} {ans}')