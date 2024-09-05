import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(N)]
price = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(N):
    result = 0
    for j in range(5):
        result += lst[i][j] * price[j]
    print(f'${format(result, ".2f")}')