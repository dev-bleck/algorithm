import sys
sys.stdin = open('sample_input.txt')


def is_palindrome(word):
    return word == word[::-1]


def solve(word, sub_len):
    cnt = 0
    for idx in range(len(word) - sub_len + 1):
        if is_palindrome(word[idx:idx + sub_len]):
            cnt += 1
    return cnt


for test_case in range(1, 11):
    word_len = int(input())
    size = 8

    col = []
    row = [''] * size
    for _ in range(size):
        word = input()
        col.append(word)
        for i in range(size):
            row[i] += word[i]

    # col과 row가 들고 있는 단어들 중 길이가 word_len인 회문의 갯수
    result = 0
    for word in col:
        result += solve(word, word_len)

    for word in row:
        result += solve(word, word_len)

    print(f'#{test_case} {result}')
