import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbs = [list(map(str, input().split())) for _ in range(N)]

    arr1 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            arr1[y][x] = numbs[N - 1 - x][y]

    arr2 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            arr2[y][x] = arr1[N - 1 - x][y]

    arr3 = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            arr3[y][x] = arr2[N - 1 - x][y]

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(arr1[i]), end=' ')
        print(''.join(arr2[i]), end=' ')
        print(''.join(arr3[i]))
