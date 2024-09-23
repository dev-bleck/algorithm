import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_set = {input().rstrip() for _ in range(N)}
M_lst = list(input().rstrip() for _ in range(M))
cnt = 0

for i in M_lst:
    if i in N_set:
        cnt += 1

print(cnt)