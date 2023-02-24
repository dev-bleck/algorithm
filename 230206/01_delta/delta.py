import sys
sys.stdin = open('sample_input.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (dx, dy) => arr[y + dy][x + dx]
# left, rigth, up, down
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # x, y

for test_case in range(1, T + 1):
    N = int(input())

    # 생각을 덜 해도 되는 방식
    # arr = []
    # for _ in range(N):
    #     arr.append(list(map(int, input().split())))

    # 생각을 더 해야 되는 방식 - list comprehension
    # 어떤게 더 빠른지는 지금 생각할 수준과 단계가 아님!
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_sum = 0
    for i in range(N): # y값
        for j in range(N): # x값
            this_sum = 0
            # print(f'i: {i}, j: {j}, arr[i][j]: {arr[i][j]}')
            # arr[i][j]
            for dir in range(4):
                cmp_x = j + dx[dir]
                cmp_y = i + dy[dir]
                if 0 <= cmp_x <= 4 and 0 <= cmp_y <= 4:
                    this_sum += abs(arr[i][j] - arr[cmp_y][cmp_x])
            total_sum += this_sum

    print(f'#{test_case} {total_sum}')