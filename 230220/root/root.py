import sys
sys.stdin = open('../../230221/sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    X = None
    i = 1
    while not X:
        if i * i * i == N:
            X = i
        elif i * i * i > N:
            X = -1
        i += 1

    print(f'#{test_case} {X}')
