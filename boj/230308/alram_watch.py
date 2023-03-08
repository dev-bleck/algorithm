H, M = map(int, input().split())
if H == 0:
    H = 24
time = H * 60 + M
H = (time - 45) // 60
if H == 24:
    H = 0
M = (time - 45) % 60
print(H, M)