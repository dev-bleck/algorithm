import sys
sys.stdin = open('sample_input.txt')

def len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = len(arr)
    bit = [0] * N
    for i in range(1, 1 << N): # 2 ** N # 0부터 반복하면 공집합 때문에 무조건 성공
        subset_sum = 0 # 이번 반복의 부분집합의 합을 저장
        for j in range(N):
            if i & (1 << j):
                # print(arr[j], end=' ')
                subset_sum += arr[j]
        # print()
        if subset_sum == 0:
            print(f'#{test_case} 1')
            break
    else:
        print((f'#{test_case} 0'))


for i in range(1, 1 << N): # 2 ** N # 0부터 반복하면 공집합 때문에 무조건 성공
    print(f'i: {i}, ', end='')
    for j in range(N): # j for문이 다 돌면 부분집합 1개
        if i & (1 << j):
            print(arr[j], end=' ')
    print()