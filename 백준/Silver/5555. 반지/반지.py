import sys
input = sys.stdin.readline

word = str(input().rstrip())
N = int(input())
lst = []
for i in range(N):
    ring = str(input().rstrip())
    ring += ring[0:len(word)]
    lst.append(ring)
cnt = 0

for i in range(N):
    for j in range(10):
        if word == lst[i][j:j + len(word)]:
            cnt += 1
            break

print(cnt)