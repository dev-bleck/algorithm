import sys
input = sys.stdin.readline

N, D = map(int, input().split())
lst = [str(i) for i in range(1, N + 1)]
cnt = 0

for i in lst:
    for j in i:
        if j == str(D):
            cnt += 1

print(cnt)