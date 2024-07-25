import sys
input = sys.stdin.readline

N = list(input().rstrip())
lst = [0 for _ in range(10)]

for i in range(10):
    if i == 6:
        lst[9] += N.count(str(i))
    else:
        lst[i] += N.count(str(i))

lst[9] = lst[9] // 2 + lst[9] % 2
print(max(lst))