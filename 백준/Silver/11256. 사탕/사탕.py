import sys
input = sys.stdin.readline

for _ in range(int(input())):
    J, N = map(int, input().split())  # J: 사탕 개수, N: 크기가 다른 상자 개수
    lst = []
    for _ in range(N):
        R, C = map(int, input().split())  # R: 상자의 세로 길이, C: 상자의 가로 길이
        lst.append(R * C)
        lst.sort(reverse=True)

    for i in range(N):
        if sum(lst[0:i]) >= J:
            print(i)
            break