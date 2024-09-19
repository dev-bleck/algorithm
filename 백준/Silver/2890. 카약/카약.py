import sys
input = sys.stdin.readline

R, C = map(int, input().split())
lst = sorted([str(input().rstrip()[::-1]) for _ in range(R)], reverse=True)
res = [[] for _ in range(C)]

for i in range(R):
    cnt = 0
    for j in range(1, C - 1):
        if lst[i][j] != '.':
            res[cnt].append(int(lst[i][j]))
            break
        else:
            cnt += 1

res = [i for i in res if i != []]

rank = 1
result = [0] * 10
for i in res:
    for j in i:
        result[j] = rank
    rank += 1

for i in range(1, 10):
    print(result[i])