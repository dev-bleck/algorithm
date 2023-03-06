import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 방법1. 오름차순 정렬 후 반복
    arr = sorted(arr)

    minV = 1000
    for i in range(N - 2):  # 소 박스
        for j in range(i + 1, N - 1):  # 중 박스
            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:  # 같은 크기가 다른 박스에 들어가는 경우 제외
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A*B*C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)

    if minV == 1000:
        minV = -1


    # 방법2. count 배열
    size = [0] * 31     # 당근의 크기 1 ~ 30
    for c in arr:       # 크기별로 개수 파악
        size[c] += 1

    minV = 1000
    for i in range(29):  # i : 1 ~ 28 소 박스에 들어갈 크기
        for j in range(30):  # i + 1 ~ 29 : 중 박스에 들어갈 크기
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:31])
            if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                diff = max(A, B, C) - min(A, B, C)
                if minV > diff:
                    minV = diff

    if minV == 1000:
        minV = -1

    print(f'#{test_case} {minV}')