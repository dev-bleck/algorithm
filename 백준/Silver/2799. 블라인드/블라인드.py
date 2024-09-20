import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(M * 4 + M + 1)]
a = b = c = d = e = 0

for x in range(1, N * 5 + 1, 5):
    for y in range(1, M * 4 + M + 1, 5):
        if lst[y][x] == '.':
            a += 1
        else:
            if lst[y + 1][x] == '.':
                b += 1
            else:
                if lst[y + 2][x] == '.':
                    c += 1
                else:
                    if lst[y + 3][x] == '.':
                        d += 1
                    else:
                        e += 1

print(a, b, c, d, e)