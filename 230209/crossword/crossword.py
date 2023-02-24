import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    strings = [list(map(int, input().split())) for _ in range(N)]
    fit = 0  # 정확히 맞아들어가면 증가

    # 가로
    for y in range(N):
        cnt = 0  # 1이 나온 횟수를 셈
        for x in range(N):
            if strings[y][x] == 1 or (strings[y][x] == 1 and x == N-1):  # 현 위치가 1이거나, 1이면서 퍼즐의 끝이면,
                cnt += 1  # cnt 1 증가
            else:  # 현 위치가 0일 때
                if cnt == K:  # 현재 1이 나온 횟수가 특정 길이 K와 같으면
                    fit += 1  # fit 1 증가
                cnt = 0  # cnt 초기화
        if cnt == K:  # for문이 다 돌았을 때, cnt == K이면
            fit += 1  # fit 1 증가

    # 세로
    for x in range(N):
        cnt = 0
        for y in range(N):
            if strings[y][x] == 1 or (strings[y][x] == 1 and x == N-1):  # 현 위치가 1이거나, 1이면서 퍼즐의 끝이면,
                cnt += 1  # cnt 1 증가
            else:  # 현 위치가 0일 때
                if cnt == K:  # 현재 1이 나온 횟수가 특정 길이 K와 같으면
                    fit += 1  # fit 1 증가
                cnt = 0  # cnt 초기화
        if cnt == K:  # for문이 다 돌았을 때, cnt == K이면
            fit += 1  # fit 1 증가

    print(f'#{test_case} {fit}')  # 결과(정확히 맞아들어간 횟수) 출력
