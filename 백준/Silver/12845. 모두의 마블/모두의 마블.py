import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())), reverse=True)
tmp_level = lst[0]
gold = 0

if N == 1:
    gold = tmp_level
else:
    for i in range(1, N):
        tmp_level = max(tmp_level, lst[i])
        gold += tmp_level + lst[i]

print(gold)