import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    lst = list(str(input().rstrip()) for _ in range(K))
    answer = 0

    for i in range(K):
        for j in range(i + 1, K):
            word1 = lst[i] + lst[j]
            word2 = lst[j] + lst[i]
            if word1 == word1[::-1]:
                answer = word1
            elif word2 == word2[::-1]:
                answer = word2

    print(answer)