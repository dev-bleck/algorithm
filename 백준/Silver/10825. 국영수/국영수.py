import sys
input = sys.stdin.readline

N = int(input())
grades = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(N)]
grades.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in grades:
    print(i[0])