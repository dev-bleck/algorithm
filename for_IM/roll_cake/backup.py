L = int(input())
N = int(input())
rollcake = [1] * (L+1)


max_cnt = 0
max_diff = 0
for i in range(1, N + 1):
    s, e = map(int, input().split())
    if max_diff < abs(s - e + 1):
        max_diff = abs(s - e + 1)
        ans1 = i + 1

    cnt = sum(rollcake[s:e+1])
    if cnt > max_cnt:
        max_cnt = cnt
        ans2 = i + 1

print(ans1)
print(ans2)