import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    palindrome = word[::-1]

    if word == palindrome:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
