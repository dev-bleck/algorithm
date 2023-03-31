import sys
sys.stdin = open('sample_input.txt')


def dfs(n, sm):
    global ans
    # 최소값 구할 때 항상(?) 성공하는 가지치기
    if ans < sm:
        return

    if n > 12:
        ans = min(ans, sm)
        return

    dfs(n + 1, sm + day * lst[n])   # 일간권
    dfs(n + 1, sm + mon)            # 월간권
    dfs(n + 3, sm + mon3)           # 분기권
    dfs(n + 12, sm + year)          # 연간권


T = int(input())

for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    # [방법 1] 백트래킹
    ans = 365 * 3000
    dfs(0, 0)

    # [방법 2] 규칙성 찾기
    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달까지의 최소 비용
        s[i] = s[i - 1] + day * lst[i]          # 일간권
        s[i] = min(s[i], s[i - 1] + mon)        # 월간권
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + mon3)   # 분기권
        if i >= 12:
            s[i] = min(s[i], s[i - 12] + year)  # 연간권

    ans = s[12]

    print(f'#{test_case} {ans}')