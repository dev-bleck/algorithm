import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    i = ans = 0
    while i < N:
        # [1] i ~ 끝까지 최대값의 index 찾기
        i_mx = i
        for j in range(i+1, N):  # i의 인덱스는 했으니까 다음 것 부터
            if lst[i_mx] < lst[j]:
                i_mx = j
        # [2] i ~ i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]

        i = i_mx + 1
    print(f'#{test_case} {ans}')