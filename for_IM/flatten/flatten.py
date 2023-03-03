import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    dump = int(input())
    arr = sorted(list(map(int, input().split())))
    while dump != 0:
        arr[0] += 1
        arr[-1] -= 1
        arr = sorted(arr)
        dump -= 1
    ans = max(arr) - min(arr)
    print(f'#{test_case} {ans}')