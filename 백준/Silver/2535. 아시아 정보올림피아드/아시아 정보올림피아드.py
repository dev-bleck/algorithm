import sys
input = sys.stdin.readline

N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[2], reverse=True)
check = [0 for _ in range(100)]
answer = []

for i in range(N):
    if check[lst[i][0]] < 2:
        check[lst[i][0]] += 1
        answer.append([lst[i][0], lst[i][1]])

    if len(answer) == 3:
        break

for i in answer:
    print(*i)