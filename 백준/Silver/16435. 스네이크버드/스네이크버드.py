import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for i in lst:
    if L >= i:
        L += 1
        
print(L)