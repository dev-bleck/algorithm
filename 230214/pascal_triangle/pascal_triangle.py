import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())
    tmp = []
    print(1)  # 꼭대기 1
    for i in range(N - 1):
        result = [1]  # 2번째 줄의 왼쪽 끝 1

        # 이전 결과를 참조한 중간값들
        for j in range(i):
            result.append(tmp[j] + tmp[j + 1])

        result.append(1)  # 다음 줄의 오른쪽 끝 1

        print(*result)
        # 다음에 사용하기 위해 저장
        tmp = result