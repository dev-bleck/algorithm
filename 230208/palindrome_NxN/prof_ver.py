import sys
sys.stdin = open('sample_input.txt')


def contains_palindrome(word, pal_len):
    idx = 0
    # while은 word에 사용할 인덱스 끝 값
    # 이 word의 최대 인덱스 값 보다 작을 동안
    while idx + pal_len - 1 < len(word):  # 0 ~ + M - 1
        target = word[idx:idx + pal_len]  # substring : 부분 문자열

        # 초심자의 회문 검사
        if target == target[::-1]:
            return target

        idx += 1


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = ''
    # 한 for문에 가로세로 다 구하기
    for i in range(N):
        word_horizontal = arr[i]  # i행 가로 단어
        result = contains_palindrome(word_horizontal, M)
        if result:
            break

        word_vertical = ''        # i열 세로 단어
        for j in range(N):
            word_vertical += arr[j][i]

        result = contains_palindrome(word_vertical, M)
        if result:
            break

    print(f'#{test_case} {result}')
