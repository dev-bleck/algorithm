import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    strings = [input() for _ in range(N)]

    palindrome = ''
    for i in range(N-M+1):
        for y in range(N):
            result = ''
            for x in range(M):
                result += strings[y][x+i]
            if result == result[::-1]:
                palindrome = result

        for x in range(N):
            result = ''
            for y in range(M):
                result += strings[y+i][x]
            if result == result[::-1]:
                palindrome = result

    print(f'#{test_case} {palindrome}')
