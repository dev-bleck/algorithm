import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst = lst[::-1]
res = 0

for i in range(N - 1):
    if lst[i] <= lst[i + 1]:
        res += abs(lst[i] - lst[i + 1]) + 1
        lst[i + 1] -= abs(lst[i] - lst[i + 1]) + 1

print(res)