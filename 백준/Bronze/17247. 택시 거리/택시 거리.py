import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
res = []

for x in range(N):
    for y in range(M):
        if lst[x][y] == 1:
            res.append([x, y])

print(abs(res[0][0] - res[1][0]) + abs(res[0][1] - res[1][1]))