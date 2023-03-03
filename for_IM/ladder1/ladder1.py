import sys

sys.stdin = open('sample_input.txt')

T = 10

for test_case in range(1, T + 1):
    delta_x = [0, -1, 1]
    delta_y = [-1, 0, 0]

    _ = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        if ladder[99][x] == 2:
            answer_x = x
            answer_y = 99

    while answer_y != 0:
        for i in range(3):
            new_x = answer_x + delta_x[i]
            new_y = answer_y + delta_y[i]
            if 0 <= new_x < 100 and 0 <= new_y < 100 and ladder[new_y][new_x] == 1:
                ladder[new_y][new_x] = 0
                answer_x = new_x
                answer_y = new_y

    print(f'#{test_case} {answer_x}')