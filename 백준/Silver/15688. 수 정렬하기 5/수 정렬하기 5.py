import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(int(input()) for _ in range(N)), reverse=False)
for i in lst:
    print(i)