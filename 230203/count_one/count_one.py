# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test case count input
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 수열의 길이
    arr = input()  # 수열
    count = result = 0  # 1이 나온 횟수, 결과값
    final_result = 0 # 최종 결과

    for i in range(len(arr)):  # 수열의 길이만큼 반복
        if int(arr[i]) == 1:  # 현재 인덱스의 값이 1이면
            count += 1  # 1이 나온 횟수 1 증가
            result = count  # 결과값에 횟수 할당

        if final_result < result: # 현재 최종 결과보다 결과값이 크면
            final_result = result # 최종 결과에 결과값 할당

        if int(arr[i]) == 0 :  # 현재 인덱스의 값이 0이면
            if result > len(arr[i:]):  # 현재 결과가 남은 수열의 길이보다 크면
                break  # 반복문 종료
            count = 0  # 횟수 0으로 초기화

    print(f'#{test_case} {final_result}')  # 최종 결과 출력