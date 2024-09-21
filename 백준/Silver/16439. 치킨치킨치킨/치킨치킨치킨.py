import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
preference = [list(map(int, input().split())) for _ in range(N)]
max_pref = 0

for a, b, c in combinations(range(M), 3):
    now_pref = 0

    for i in range(N):
        now_pref += max(preference[i][a], preference[i][b], preference[i][c])

    max_pref = max(max_pref, now_pref)

print(max_pref)