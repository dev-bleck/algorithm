L = int(input())
rollcake = [1] * L
N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

max_cnt = 0
max_diff = 0
for i in range(N):
    s, e = lst[i][0], lst[i][1]
    if max_diff < abs(e - s + 1):
        max_diff = abs(e - s + 1)
        ans1 = i + 1
        print(abs(e - s + 1), ans1)
    cnt = 0
    for j in range(s, e + 1):
        if rollcake[j] == 1:
            rollcake[j] = 0
            cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            ans2 = i + 1

print(ans1)
print(ans2)