import sys
input = sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for i in range(N, M + 1):
            if len(str(i)) == len(set(str(i))):
                cnt += 1
        print(cnt)
    except ValueError:
        break