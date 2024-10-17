import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 1

for y in range(N):
    for x in range(M):
        for i in range(1, min(N, M)):
            if y + i < N and x + i < M:
                if rectangle[y][x] == rectangle[y + i][x] == rectangle[y][x + i] == rectangle[y + i][x + i]:
                    answer = max(answer, (i + 1) ** 2)

print(answer)