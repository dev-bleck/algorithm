import sys
sys.stdin = open('sample_input.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

now_min = M
for x in range(N):
    for y in range(x + 1, N):
        for z in range(y + 1, N):
            now_sum = cards[x] + cards[y] + cards[z]
            if now_min > (M - now_sum) >= 0:
                now_min = M - now_sum
                ans = now_sum

print(ans)