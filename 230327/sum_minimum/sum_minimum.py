import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(f'#{test_case} {arr}')