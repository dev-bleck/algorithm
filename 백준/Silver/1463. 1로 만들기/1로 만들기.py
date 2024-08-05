import sys
input = sys.stdin.readline


def dp(cur):
    memo = [0] * (cur + 1)

    for i in range(2, cur + 1):
        memo[i] = memo[i - 1] + 1
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)

    return memo[cur]


print(dp(int(input().rstrip())))