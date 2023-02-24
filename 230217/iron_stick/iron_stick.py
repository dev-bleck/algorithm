import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    st = input()
    cnt = ans = 0
    for i in range(len(st)):
        if st[i] == '(':  # 막대기 시작 or 레이저
            cnt += 1
        else:
            cnt -= 1
            if st[i-1] == '(':  # 레이저
                ans += cnt
            elif st[i-1] == ')':  # ')' 직전의 괄호를 확인
                ans += 1

    print(f'#{test_case} {ans}')