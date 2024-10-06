import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
lst = sorted(list(int(input()) for _ in range(N)))

answer1 = 0
answer2 = abs(A - B)

if B in lst:
    answer1 = 1
else:
    for i in lst:
        if answer2 > abs(i - B):
            answer2 = abs(i - B) + 1
        else:
            answer1 = abs(A - B)

if answer1 == 0:
    answer1 = answer2
elif answer2 == 0:
    answer2 = answer1

if answer2 > answer1:
    print(answer1)
else:
    print(answer2)