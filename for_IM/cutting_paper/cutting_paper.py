C, R = map(int, input().split())
r_lst = [0, R]
c_lst = [0, C]

N = int(input())

for _ in range(N):
    t, n = map(int, input().split())
    if t == 0:
        r_lst.append(n)
    else:
        c_lst.append(n)

r_lst.sort()
c_lst.sort()

r_max, c_max = 0, 0
for i in range(1, len(r_lst)):
    if r_max < r_lst[i] - r_lst[i-1]:
        r_max = r_lst[i] - r_lst[i-1]

for i in range(1, len(c_lst)):
    if c_max < c_lst[i] - c_lst[i-1]:
        c_max = c_lst[i] - c_lst[i-1]

print(r_max * c_max)
