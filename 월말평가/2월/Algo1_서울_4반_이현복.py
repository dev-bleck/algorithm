T = int(input())  # test_case input

for test_case in range(1, T + 1):
    # N : 행의 개수 / M : 열의 개수
    N, M = map(int, input().split())

    garden = []  # garden : 정원의 영역을 input 받을 리스트
    for _ in range(N):  # 행의 개수만큼 정원의 영역 input
        garden.append(list(map(int, input().split())))

    trees = []  # trees : 한 줄씩 띄워서 심는 나무만 할당할 리스트
    for y in range(0, N + 1, 2):  # 한 칸씩 띄워주기 위해 2씩 반복
        now_trees = []  # now_trees : 한 열을 리스트로 저장하기 위한 임시 리스트
        for x in range(N):
            now_trees.append(garden[x][y])  # 심은 나무들을 임시 리스트에 추가
        trees.append(now_trees)  # 임시 리스트에 추가된 나무를 최종적으로 심는 나무만 저장하는 리스트에 추가

    # sum_cost : 나무를 심는 총 비용 / sum_trees : 심은 나무의 수
    # now_max : 현재 가장 비싼 나무 / max_col : 가장 비싼 나무가 심어진 열
    sum_cost, sum_trees, now_max, max_col = 0, 0, 0, 0  # 변수 값 초기화
    for idx, i in enumerate(trees):  # enumrate를 사용해서 index와 값을 함께 사용
        sum_trees += len(i)  # 심은 나무의 수 => 열의 개수를 세서 더하고 저장
        if now_max <= max(trees[idx]):  # 현재 최대값 보다 현재 나무의 최대값이 크거나 같으면
            now_max = max(trees[idx])  # 현재 최대값 갱신
            max_col = idx * 2 + 1  # 현재 최대값 나무의 열
            # idx * 2 + 1 : 문제에서 열이 1번부터 시작하고, 2칸 씩 띄워서 심기 때문에.
            if max_col < idx * 2 + 1:  # 최대값은 같지만 가장 큰 열의 번호를 계산하기 위해
                max_col = idx * 2 + 1  # 열이 더 크면 갱신
        for j in range(len(i)):  # 나무를 심는 총 비용 계산
            sum_cost += i[j]  # 열마다 나무의 값을 더해서 저장

    # 나무를 심는 총 비용, 심은 나무의 수, 가장 비싼 나무의 가격, 가장 비싼 나무가 심어진 열 출력
    print(f'#{test_case} {sum_cost} {sum_trees} {now_max} {max_col}')
