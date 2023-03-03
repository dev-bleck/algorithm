import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    _ = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    delta_x = [-1, 1, 0]
    delta_y = [0, 0, 1]

    min_cnt = 100*100
    for i in range(100):
        visited = [[0] * 100 for _ in range(100)]
        if ladder[0][i] == 1:
            cnt = 0
            x = i
            y = 0
            while y != 99:
                    for j in range(3):
                        new_x = x + delta_x[j]
                        new_y = y + delta_y[j]
                        if (0 <= new_x < 100 and 0 <= new_y < 100) and ladder[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                            visited[new_y][new_x] = 1
                            x = new_x
                            y = new_y
                            cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt
                ans = i

    print(f'#{test_case} {ans}')
