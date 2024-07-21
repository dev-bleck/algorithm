import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [str(input().rstrip()) for _ in range(N)]

white_first = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
black_first = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
res = 1e9

for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = cnt2 = 0
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != white_first[x][y]:
                    cnt1 += 1

        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != black_first[x][y]:
                    cnt2 += 1

        res = min(res, cnt1, cnt2)

print(res)