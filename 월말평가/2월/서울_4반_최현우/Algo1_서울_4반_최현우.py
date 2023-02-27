# 테스트 케이스 갯수 입력
t = int(input())

for test_case in range(1, t+1):
    # N은 행, Y는 열
    N , M = map(int, input().split())
    # 행의 갯수 만큼 가든의 값 입력 받음
    garden = [list(map(int, input().split())) for _ in range(N)]

    # 총비용, 심은 나무의 숫자, 가장 비싼 나무의 가격, 가장 비싼 나무가 심어진 열 초기화
    total_price = 0
    trees = 0
    expensive_tree = 0
    expensive_col = 0
    # 1열 부터 행을 바꿔 가며 순회, 나무를 한칸 씩 띄어 심기 때문에 +2 를 해줘야함
    for j in range(0, M, +2):
        for i in range(N):
            total_price += garden[i][j]  # 각 위치의 나무의 값 더하기
            trees += 1 # 순회하는 위치 횟수 더하기
            # 비싼 나무의 값과 열 계산
            if garden[i][j] >= expensive_tree: # 비싼 나무가 있는 열이 여러개라면 가장 뒤에 있는 것을 출력
                expensive_tree = garden[i][j] # 비싼 나무의 값을 새로 저장
                expensive_col = j+1  # 비싼 나무의 값의 열을 저장, list의 인덱스는 0부터 시작하기 때문에 col에 + 1 해줘야함

    print(f'#{test_case} {total_price} {trees} {expensive_tree} {expensive_col}')


