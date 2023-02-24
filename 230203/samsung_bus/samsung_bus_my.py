import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5000

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            cnt[i] += 1

    P = int(input())
    lst = []
    for _ in range(P):
        C = int(input())
        lst.append(cnt[C])

    print(f'#{test_case}', *lst)