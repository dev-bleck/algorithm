# 테스트 케이스의 갯수
t = int(input())

for test_case in range(1, t+1):
    # N은 하늘의 크기 K는 카메라의 영역, (A,B)는 초점 A가 행, B가 열, 입력값은 0 부터 시작
    N, K, A, B = map(int,input().split())
    sky = [list(input().split()) for _ in range(N)]

    # 하늘에 있는 * 의 갯수를 확인 한 후 카메라의 영역 내에서 해당 갯수와 같은 양의 별이 있는지 확인
    stars = 0
    for i in range(N):
        for j in range(N):
            if sky[i][j] =='*':
                stars += 1

    # (A, B)를 기준으로 좌 우 K //2 만큼 관측해야함 홀수이므로, K//2를 해주면 됨
    scope_range = K // 2
    # 망원경의 배율
    scope = 0
    while True:
        # 현재 배율에서 관측되는 별의 갯수 초기화
        tmp_stars = 0
        # 카메라의 영역 내에서 관측되는 별의 갯수 세기
        for i in range(A-scope_range, A+scope_range+1): # +1을 해주는 것은 A+scope_range까지 확인해야 하기 때문입니다.
            for j in range(B-scope_range, B+scope_range+1):
                # i와 j의 범위가 하늘을 벗어나지 않도록 설정
                if N > i >= 0 and N > j >= 0:
                    # 해당 위치가 별이면 관측되는 별의 갯수에 +1
                    if sky[i][j] == '*':
                        tmp_stars += 1
        # 관측된 별의 갯수와, 찍으려고 하는 별의 갯수가 같다면 스코프를 한번 확대시킴.
        if tmp_stars == stars:
            scope += 1
            # 스코프를 한번 확대시키면 찍으려는 범위가 양쪽으로 줄어들어 범위가 총 2만큼 줄어듬
            scope_range -= 1
        # 만약 scope가 0인데 찍으려는 별의 갯수와 찍힌 별의 갯수가 같지 않다면 관측이 불가능한 것
        # 그 외에는 관측되는 별의 갯수와 찍으려는 별의 갯수가 다른 경우 while문을 break해줌
        # scope값을 하나 빼주는 이유는, 해당 배율로 별을 다 관측하지 못하는 경우라서 마지막 성공한 scope값만 리턴해주기 위함
        # 마찬가지로 scope값이 0 (기본값)인 경우에도 관측하지 못한다면 scope 값을 1 빼서 -1을 리턴하게 해줌
        else:
            scope -= 1
            break
    print(f'#{test_case} {scope}')