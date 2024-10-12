import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
numbs = list(map(int, input().split()))
numbs_permutations = list(permutations(numbs))
answer = 0

for permutation in numbs_permutations:
    now_answer = 0
    for i in range(N - 1):
        now_answer += abs(permutation[i] - permutation[i + 1])

    answer = max(answer, now_answer)

print(answer)