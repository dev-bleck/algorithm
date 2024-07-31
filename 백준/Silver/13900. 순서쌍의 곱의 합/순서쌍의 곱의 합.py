import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

total_sum = sum(lst)
res = 0

for num in lst:
    total_sum -= num
    res += num * total_sum

print(res)