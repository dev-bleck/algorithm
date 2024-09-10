import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
lst2 = [list(map(int, input().split())) for _ in range(M)]

res = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            res[i][j] += lst1[i][k] * lst2[k][j]

for i in res:
    print(' '.join(map(str, i)))