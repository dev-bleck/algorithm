import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]

    for _ in range(N):
        for i in range(N):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(f'#{test_case}', end=" ")
    for i in range(1, 6):
        print(arr[-i], end=" ")
        print(arr[i], end=" ")
    print()