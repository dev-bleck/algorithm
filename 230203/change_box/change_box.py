# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # test_case

for test_case in range(1, T + 1):
    N, Q = map(int, input().split()) # N : 상자 개수 / Q : 변경 횟수
    cnt = [0] * N # 최초에 0으로 적혀 있는 상자 list

    for i in range(1, Q + 1): # i = 1일 때부터 i = Q일 때까지 반복
        # L : 왼쪽 시작 상자 / R : 오른쪽 시작 상자
        L, R = map(int, input().split())
        # 시작 범위에 -1을 해야 0번째 인덱스부터 시작 가능
        for j in range(L - 1, R):
            cnt[j] = i # j번째 인덱스에 i값 할당

    print(f'#{test_case}', *cnt) # 상자에 적혀있는 값 순서대로 출력