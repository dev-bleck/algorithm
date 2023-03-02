import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = []
    for _ in range(N):
        flag.append(list(map(str, input())))

    print(f'#{test_case} {flag}')