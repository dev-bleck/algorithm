import sys
input = sys.stdin.readline


def recur(cur):
    if cur < 0:
        return True

    if cur == 0:
        return False

    if dp[cur] != -1:
        return dp[cur]

    cnt = 0
    for i in arr:
        if not recur(cur - i):
            cnt += 1

    if cnt > 0:
        dp[cur] = cnt
        return dp[cur]
    else:
        dp[cur] = cnt
        return dp[cur]


N = int(input())
arr = [1, 3]
dp = [-1] * (N + 1)

if recur(N):
    print('SK')
else:
    print('CY')