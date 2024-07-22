import sys
input = sys.stdin.readline

N = int(input())
lst = list(int(input()) for _ in range(N))
left = right = 0

max_left = max_right = 0
for i in range(N):
    if lst[i] > max_left:
        max_left = lst[i]
        left += 1

lst = lst[::-1]
for i in range(N):
    if lst[i] > max_right:
        max_right = lst[i]
        right += 1

print(left)
print(right)