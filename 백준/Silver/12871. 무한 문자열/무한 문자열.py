import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip()) * 50
res = 0

for i in range(len(t) // len(s)):
    if t[i * len(s):i * len(s) + len(s)] == s:
        res = 1
    else:
        res = 0
        break

print(res)