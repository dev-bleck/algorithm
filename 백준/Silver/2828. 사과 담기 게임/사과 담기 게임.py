import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

move = 0
l, r = 1, M

for _ in range(J):
    location = int(input())
    
    if l <= location <= r:
        continue

    if l > location:
        move += l - location
        r -= l - location
        l = location
    elif r < location:
        move += location - r
        l += location - r
        r = location

print(move)