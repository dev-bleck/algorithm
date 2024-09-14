import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
paint = [[M] * 101 for _ in range(101)]

for i in lst:
    for x in range(i[0], i[2] + 1):
        for y in range(i[1], i[3] + 1):
            if paint[x][y] > -1:
                paint[x][y] -= 1

res = 0

for i in paint:
    res += i.count(-1)

print(res)