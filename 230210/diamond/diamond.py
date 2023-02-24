import sys
sys.stdin = open('sample_input.txt')


def diamond(even, odd):
    if i % 2 == 0:  # 짝수번째 인덱스일 때
        res = even
    else:  # 홀수번째 인덱스일 때
        res = odd
    return print(res, end="")


T = int(input())
for test_case in range(T):
    strings = [a for a in input()]

    for i in range(len(strings)):
        diamond('..#..', '.#.')
        # 홀수이고, 현재 인덱스가 마지막 인덱스이고, 전체 문자열의 길이가 1이 아닐 때,
        if i % 2 == 1 and i == len(strings) - 1 and len(strings) != 1:
            # 마지막 특수문자 추가
            print('.', end="")
    print()

    for i in range(len(strings)):
        diamond('.#.#.', '#.#')
        if i % 2 == 1 and i == len(strings) - 1 and len(strings) != 1:
            print('.', end="")
    print()

    for i in range(len(strings)):
        diamond(f'#.{strings[i]}.#', f'.{strings[i]}.')
        if i % 2 == 1 and i == len(strings) - 1 and len(strings) != 1:
            print('#', end="")
    print()

    for i in range(len(strings)):
        diamond('.#.#.', '#.#')
        if i % 2 == 1 and i == len(strings) - 1 and len(strings) != 1:
            print('.', end="")
    print()

    for i in range(len(strings)):
        diamond('..#..', '.#.')
        if i % 2 == 1 and i == len(strings) - 1 and len(strings) != 1:
            print('.', end="")
    print()