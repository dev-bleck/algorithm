import sys
sys.stdin = open('sample_input.txt')

def len(array):
    count = 0
    for _ in array:
        count += 1
    return count

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    actual_numbers = list(map(int, input().split()))

    for _ in range(len(actual_numbers)):
        for i in range(0, len(actual_numbers) - 1):
            if actual_numbers[i] > actual_numbers[i+1]:
                actual_numbers[i], actual_numbers[i+1] = actual_numbers[i+1], actual_numbers[i]

    arr = [[0 for _ in range(N)] for _ in range(N)]
    x = y = 0
    cnt = 0
    arr[y][x] = actual_numbers[cnt]
    delta_x = [1, 0, -1, 0]
    delta_y = [0, 1, 0, -1]

    dir_idx = 0
    cnt = 1
    while cnt < N ** 2:
        new_x = x + delta_x[dir_idx]
        new_y = y + delta_y[dir_idx]

        if (0 <= new_x < N and 0 <= new_y < N) and arr[new_y][new_x] == 0:
            arr[new_y][new_x] = actual_numbers[cnt]
            x, y = new_x, new_y
            cnt += 1
        elif dir_idx == 3:
            dir_idx = 0
        else:
            dir_idx += 1

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()