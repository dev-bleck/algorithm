import sys
sys.stdin = open('sample_input.txt')

N = 101
M = 10
papers = int(input())
position = [list(map(int, input().split())) for _ in range(papers)]
colored = [[0] * N for _ in range(N)]

for i in range(papers):
    a, b = position[i][0], position[i][1]
    for y in range(b, b + M):
        for x in range(a, a + M):
            colored[y][x] = 1

delta_x = [0, 0, -1, 1]
delta_y = [-1, 1, 0, 0]
count = 0
for y in range(1, N - 1):
    for x in range(1, N - 1):
        for i in range(4):
            new_x = x + delta_x[i]
            new_y = y + delta_y[i]
            if 0 <= new_x < N and 0 <= new_y < N and colored[y][x] == 1:
                if colored[new_y][new_x] == 0:
                    count += 1

print(count)