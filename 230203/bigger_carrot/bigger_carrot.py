# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # test_case

for test_case in range(1, T + 1):
    N = int(input()) # N : 당근의 개수
    N_list = list(map(int, input().split())) # 각 당근의 크기가 담긴 list
    cnt = 1 # 연속으로 커지는 횟수
    result = 1 # 결과값

    for idx in range(N - 1): # 인덱싱을 위해 당근의 개수 - 1만큼 반복
        if N_list[idx] < N_list[idx + 1]: # 현재 당근의 크기보다 다음 당근의 크기가 크면
            cnt += 1 # 연속으로 커지는 횟수 1 증가
            result = cnt # 현재 cnt를 결과값에 저장
        else:
            cnt = 1 # 연속으로 커지지 않을 경우 cnt는 1로 초기화

    print(f'#{test_case} {result}') # 결과값 출력