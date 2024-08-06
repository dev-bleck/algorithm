import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = list(map(int, input().split()))

total_sum = sum(lst)
res = 0

for num in lst:
    total_sum -= num
    res = (res + num * total_sum) % 1000000007

print(res)