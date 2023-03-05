import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    for y in range(9):
        lst = []
        for x in range(9):
            lst.append(sudoku[y][x])
        if len(set(lst)) != 9:
            ans = 0

    for x in range(9):
        lst = []
        for y in range(9):
            lst.append(sudoku[y][x])
        if len(set(lst)) != 9:
            ans = 0

    for x in range(0, 7, 3):
        lst = []
        for y in range(3):
            lst.append(sudoku[y][x:x+3])

        tmp = []
        for j in range(3):
            for i in range(len(lst[0])):
                tmp.append(lst[j][i])

        if len(set(tmp)) != 9:
            ans = 0

    print(f'#{test_case} {ans}')