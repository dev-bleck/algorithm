import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    s = input()
    arr = []
    for idx in s:
        arr.append(idx)
    for idx in range(len(arr) + 1):
        if arr[idx] == arr[idx + 1]:
            arr.pop(idx)
            arr.pop(idx)
    print(f'#{test_case} {arr}')
