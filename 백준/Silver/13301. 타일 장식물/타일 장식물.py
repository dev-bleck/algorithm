import sys
input = sys.stdin.readline

N = int(input())

res = [1, 1]
for i in range(1, N + 1):
    res.append(res[i] + res[i - 1])
    
print(res[-1] * 2)