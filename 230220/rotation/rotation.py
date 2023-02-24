import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numb_list = list(map(int, input().split()))
    for _ in range(M):
        now = numb_list.pop(0)
        numb_list.append(now)

    print(f'#{test_case} {numb_list[0]}')