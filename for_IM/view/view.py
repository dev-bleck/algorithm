import sys
sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    ans = 0
    for i in range(2, len(heights) - 2):
        tmp = []
        tmp.append([heights[i] - heights[i - 2], heights[i] - heights[i - 1], heights[i] - heights[i + 1], heights[i] - heights[i + 2]])
        if min(tmp[0]) > 0:
            ans += min(tmp[0])
    print(f'#{test_case} {ans}')