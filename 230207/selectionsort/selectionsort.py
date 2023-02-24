'''
7
7 2 5 3 4 6 4
'''

N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 1): # 주어진 작업 구간의 시작 인덱스
    minIdx = i # 맨 앞 원소가 최소라 가정
    for j in range(i + 1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)