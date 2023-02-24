# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # test_case

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N : 배열 크기 / M : 파리채 크기

    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 input

    death_total = 0 # 죽은 파리의 개수 최종 결과
    for i in range(N - M + 1): # 이중 for문 사용 배열 순회
        for j in range(N - M + 1): # 범위를 N - M + 1로 해야 원하는 범위만 체크함
            death_sum = 0 # 죽은 파리의 개수 합계
            for y_d in range(M): # y값과 x값 변화를 위한 for문
                for x_d in range(M): # M만큼 순환한다
                    x = j + x_d
                    y = i + y_d
                    death_sum += arr[y][x] # 해당 좌표의 값들의 합 = 죽은 파리의 개수 합계

            if death_total < death_sum: # 최대값 환산을 위한 조건문
                death_total = death_sum

    print(f'#{test_case} {death_total}') # 결과 반환