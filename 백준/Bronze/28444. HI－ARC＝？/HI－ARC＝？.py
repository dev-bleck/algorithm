import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

print(lst[0] * lst[1] - lst[2] * lst[3] * lst[4])