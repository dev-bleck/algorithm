import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for x in range(N):
        tmp = []
        for y in range(N):
            if table[y][x] == 1:
                if len(tmp) and tmp[-1] == 2:
                    tmp.pop()
                    count += 1
                else:
                    tmp.append(table[y][x])
            elif table[y][x] == 2:
                if len(tmp) and tmp[-1] == 1:
                    tmp.pop()
                    count += 1
                else:
                    tmp.append(table[y][x])
        print(tmp)

    print(f'#{test_case} {count}')