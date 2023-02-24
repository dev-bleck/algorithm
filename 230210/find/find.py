import sys
sys.stdin = open('sample_input.txt', encoding='utf-8')

for test_case in range(1, 11):
    N = input()
    answer = input()
    strings = input()
    print(f'#{test_case} {strings.count(answer)}')
