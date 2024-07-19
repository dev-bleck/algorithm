import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))
print(*lst)