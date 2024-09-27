import sys
input = sys.stdin.readline

N = int(input())
words = [str(input().rstrip()) for _ in range(N)]
lst = [[] for _ in range(N)]
for index in range(N):
    for i in range(len(words[index])):
        answer = ''
        for j in range(i, len(words[index]) + i):
            answer += words[index][j % len(words[index])]
        lst[index].append(answer)
    lst[index].sort()

result = set(list(map(tuple, lst)))
print(len(result))