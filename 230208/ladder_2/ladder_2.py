import sys
sys.stdin = open('sample_input.txt')

for _ in range(1, 11):
    test_case = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))


    #    좌, 우, 하
    dx = [-1, 1, 0]
    dy = [0, 0, 1]

    result = 0
    for i in range(100):  # 사다리 시작점(x : 0 ~ 99) 즉, 가로
        cnt = 0
        if ladder[0][i] == 1:  # 시작줄의 i번째가 1이면
            y = 0
            x = i
            while y != 99:  # 최하단에 도착할 때까지
                for dir_idx in range(3):
                    new_x = x + dx[dir_idx]
                    new_y = y + dy[dir_idx]

                    if (0 <= new_x < 100 and 0 <= new_y < 100) and ladder[new_y][new_x] == 1:
                        ladder[y][x] = 0  # 지나온 곳을 0으로 해줘야 무한루프 X
                        x = new_x
                        y = new_y
                        cnt += 1
                    print(x, y)
    #         if result > cnt:
    #             result = cnt
    #         print(cnt)
    #
    # print(f'#{test_case} {result}')
