import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for i in range(1, N + 1):
    if 1 <= i <= 99:
        cnt += 1
    else:
        for j in range(1, len(str(i)) - 1):
            if (int(str(i)[j - 1]) - int(str(i)[j])) != (int(str(i)[j]) - int(str(i)[j + 1])):
                break
            else:
                cnt += 1

print(cnt)