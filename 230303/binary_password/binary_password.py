import sys
sys.stdin = open('sample_input.txt')

# 직사각형 배열(code)를 받아서, 각 줄을 확인하는 함수
# 암호코드를 찾으면 바로 반환하도록 작성
def code_scanner(code):
    # 각 줄을 확인
    for row in code:
        # 모든 암호코드는 끝자리가 1
        # 그래서 뒤부터 확인하자
        # 최대값부터 한칸씩 뒤로
        for idx in range(len(row) - 1, -1, -1):
            # 0이면 다음 idx
            if row[idx] == '0':
                continue
            # 완성한 8자리 암호코드
            password = []

            # idx는 뒤에서 처음으로 1을 만난 자리
            # idx - 56 + 1 : 전체 암호코드의 시작 지점
            # (idx - 56 + 1) ~ idx까지 7자리씩 끊어서 살펴보자
            for position in range(idx - 56 + 1, idx, 7):
                # 딕셔너리에서 암호코드 찾아오기
                passcode = passcode_dict[row[position:position + 7]]
                # password에는 최종 정수 8개가 저장됨
                password.append(passcode)

            odd_digit_sum = password[0] + password[2] + password[4] + password[6]
            even_digit_sum = password[1] + password[3] + password[5] + password[7]

            if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                return odd_digit_sum + even_digit_sum
            else:
                return 0


# 이진 코드를 숫자로 만드는 딕셔너리
passcode_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{test_case} {code_scanner(arr)}')