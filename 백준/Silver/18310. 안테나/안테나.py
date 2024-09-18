import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))

if N % 2 == 0:
    ans = lst[N // 2 - 1]
else:
    ans = lst[N // 2]

print(ans)