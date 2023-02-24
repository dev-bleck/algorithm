import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    numbers = input()

    number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = ''

    for number in number_list:
        result += f'{number} ' * numbers.count(number)

    print(f'#{test_case}\n{result}')
    # print(f'#{test_case}')
    # print(*sorted_words)
