import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

total_sum = sum(lst)
square_sum = sum(x * x for x in lst)
answer = (total_sum * total_sum - square_sum) // 2

print(answer)