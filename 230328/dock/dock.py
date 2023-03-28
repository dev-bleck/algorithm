import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    last = 0
    count = 0
    lst.sort(key=lambda x: x[1])

    for i in lst:
        if last <= i[0]:
            count += 1
            last = i[1]

    print(lst)
    print(f'#{test_case} {count}')