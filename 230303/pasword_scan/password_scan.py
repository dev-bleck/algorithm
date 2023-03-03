import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 16진수 -> 2진수 dictionary
hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

# 앞쪽 0을 생략한 암호 코드
passcode_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def code_scanner(width, height, code):
    answer = 0
    # code의 높이만큼 검증
    # 윗줄을 확인하기 위해 range 활용
    for row in range(height):
        # idx는 한 줄에서 지금 확인중인 글자의 인덱스
        idx = width * 4 - 1
        # 암호 코드 8자리의 최소 길이 : 56
        # 그 때의 암호코드의 시작, 끝 인덱스 : 0 ~ 55
        # 즉, 마지막으로 확인할 인덱스는 55
        while idx > 54:  # 보다 작아지면 반복 종료
            # 1을 만나면 검증 시작 + 윗줄이 0일 때만
            if code[row][idx] == 1 and code[row - 1][idx] == 0:
                # 여기서 password 초기화를 한 것은
                password = []

                # if 내부에서 8글자를 다 찾을 예정이라는 뜻
                # for문 시작
                for _ in range(8):
                    # (0)101 => (c1) - c2 - c3 - c4의 형태(각각 0과 1이 몇번 등장했는지)
                    c2 = c3 = c4 = 0

                    # 이전 코드의 0
                    # 가장 마지막에 검증하는 부분이지만
                    # 제일 앞쪽에 와야지 정상적으로 작동
                    while code[row][idx] == 0:
                        idx -= 1

                    # 이번 코드의 4번째 부분
                    while code[row][idx] == 1:
                        # 앞으로 계속 간다
                        idx -= 1
                        c4 += 1

                    # 이번 코드의 3번째 부분
                    while code[row][idx] == 0:
                        idx -= 1
                        c3 += 1

                    # 이번 코드의 2번째 부분
                    while code[row][idx] == 1:
                        idx -= 1
                        c2 += 1

                    # 각각의 while은 숫자가 변하는 시점에 종료된다.

                    # 제일 작은걸 기준으로 비율 계산하고
                    ratio = min(c2, c3, c4)
                    # 암호에 추가
                    password.append(passcode_dict[(c2 // ratio, c3 // ratio, c4 // ratio)])
                # for문 종료 (8자리 코드 완성)

                # 짝수 & 홀수 자리 검증
                odd_digit_sum = password[1] + password[3] + password[5] + password[7]
                even_digit_sum = password[0] + password[2] + password[4] + password[6]
                if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                    answer += odd_digit_sum + even_digit_sum

            # 검증하지 않아도 앞으로 가야함
            idx -= 1

    # 결과 반환
    return answer

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]

    print(f'#{test_case} {code_scanner(M, N, arr)}')