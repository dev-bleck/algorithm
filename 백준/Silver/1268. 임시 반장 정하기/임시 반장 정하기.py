import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
same_class = [[] * N for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(5):
            if lst[i][k] == lst[j][k]:
                if j not in same_class[i]:
                    same_class[i].append(j)
                if i not in same_class[j]:
                    same_class[j].append(i)

cnt = 0
res = 0
for i in range(N):
    if len(same_class[i]) > cnt:
        cnt = len(same_class[i])
        res = i + 1

if res == 0:
    print(1)
else:
    print(res)