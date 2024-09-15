import sys
input = sys.stdin.readline

N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
cur = 0

for i in lst:
    a, n = map(int, i)

    if cur < a:
        cur = a + n
    elif cur >= a:
        cur += n

print(cur)