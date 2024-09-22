import sys
input = sys.stdin.readline

N = int(input())
numbs = sorted([int(input()) for _ in range(N)], reverse=True)

for i in numbs:
    print(i)