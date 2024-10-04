import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbs = sorted(list(map(int, input().split())), reverse=True)

answer = 0
for i in range(1, K + 1):
    answer += numbs[i - 1] - i + 1

print(answer)