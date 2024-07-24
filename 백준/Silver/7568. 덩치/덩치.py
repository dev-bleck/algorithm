import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
res = [0 for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(N):
        if lst[i][0] >= lst[j][0] and lst[i][1] >= lst[j][1]:
            continue
        elif lst[i][0] >= lst[j][0] or lst[i][1] >= lst[j][1]:
            continue
        else:
            cnt += 1
    res[i] = cnt

print(*res)