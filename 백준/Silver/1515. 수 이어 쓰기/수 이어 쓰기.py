import sys
input = sys.stdin.readline

N = str(input().rstrip())
answer = 0
index = 0

while True:
    answer += 1

    for i in str(answer):
        if i == N[index]:
            index += 1

            if index >= len(N):
                print(answer)
                exit()