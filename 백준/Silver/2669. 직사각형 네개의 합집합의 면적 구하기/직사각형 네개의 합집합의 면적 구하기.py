import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(4)]
res = [[0] * 100 for _ in range(100)]

for x1, y1, x2, y2 in lst:
    for x in range(x1, x2):
        for y in range(y1, y2):
            res[x][y] = 1

total = 0

for i in res:
    total += i.count(1)

print(total)