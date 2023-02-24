import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    tmp = [[0] * 9] * 9


    print(f'#{test_case} {sudoku}')
    print(tmp)

    # tmp에다가 횟수 더하고, tmp for문 돌려서 값이 3이 아니면 문제 있는거?