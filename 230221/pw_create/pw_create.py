import sys
sys.stdin = open('sample_input.txt')

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    numbs = list(map(int, input().split()))

    cnt = 1
    while numbs[-1] != 0:
        if cnt == 6:
            cnt = 1
        now_numb = numbs.pop(0)
        now_numb = now_numb - cnt
        numbs.append(now_numb)
        cnt += 1
        if numbs[-1] <= 0:
            numbs[-1] = 0

    print(f'#{test_case}', *numbs)
