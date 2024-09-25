import sys
input = sys.stdin.readline

H, W = map(int, input().split())
weather = [list(map(str, input().rstrip())) for _ in range(H)]
answer = [[-1] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if weather[y][x] == 'c':
            answer[y][x] = 0
        
        for z in range(1, x + 1):
            if weather[y][x - z] == 'c' and answer[y][x] == -1:
                answer[y][x] = z
                break

for lst in answer:
    print(*lst)