import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    string = [list(map(str, input())) for _ in range(5)]

    for i in range(len(string)):
        while len(string[i]) < 15:
            string[i] += ' '

    lst = []
    for x in range(15):
        for y in range(5):
            lst.append(string[y][x])

    result = "".join(lst)
    result = result.replace(' ', '')
    print(f'#{test_case} {result}')