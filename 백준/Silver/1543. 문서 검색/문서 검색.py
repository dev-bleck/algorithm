import sys
input = sys.stdin.readline

word = str(input().rstrip())
res_word = str(input().rstrip())
cnt = 0

i = 0
while i < len(word):
    if word[i:i + len(res_word)] == res_word:
        cnt += 1
        i += len(res_word)
    else:
        i += 1

print(cnt)