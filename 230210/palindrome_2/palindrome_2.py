import sys
sys.stdin = open('sample_input.txt')


def is_palindrome(word):
    return word == word[::-1]


# word == 100글자 단어
# max_size == 여태까지 찾은 최대값
def solve(word, max_size, size):
    # 현재 100자 중 word_len 글자짜리 회문이 있는지 검사
    for word_len in range(100, 0, -1):  # 큰 길이부터 작은 길이 순으로
        # 만약 word_len이 내가 아는 최대보다 작거나 같으면
        if word_len == max_size:
            # max_size가 max_size다
            break
        for idx in range(size - word_len + 1):
            # 이게 회문인지
            if is_palindrome(word[idx:idx + word_len]) and word_len > max_size:
                return word_len

    return max_size


for test_case in range(1, 11):
    input()  # 필요없엉
    size = 100
    words = [input() for _ in range(size)]

    words_ver = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += words[j][i]
        words_ver.append(tmp)

    result = 0
    for word in words:
        result = solve(word, result, size)  # 현재 최대, 후보 최대 검증

    # 세로도 동일하게
    for word in words_ver:
        result = solve(word, result, size)

    print(f'#{test_case} {result}')
