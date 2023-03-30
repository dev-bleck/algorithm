# test_row : 몇번째 줄까지 검증해야 하는지
def promising(test_row):
    for i in range(test_row):
        """
        rows[i] : 이전에 퀸을 배치해둔 줄
        rows[test_row] : 이번에 퀸을 배치한 줄
        
        실패하는 경우 두가지
        1. rows[i] == rows[test_row] : 같은 칸에 배치한 경우
        2. abs(rows[i] - rows[test_row]) == test_row - i : 대각선에 배치한 경우
        """
        if rows[i] == rows[test_row] or abs(rows[i] - rows[test_row]) == test_row - i:
            # 실패했으므로 False
            return False
    # 실패하지 않았으면 True
    return True


# current_row : 현재 퀸을 배치할 차례인 줄
def n_queen(current_row):
    if current_row == N:
        global answers
        answers += 1
    else:
        # 각 칸에다가 퀸을 배치
        for i in range(N):
            rows[current_row] = i
            # 재귀호출 전
            # 현재 보드의 상태가 조건에 맞는지 검증
            if promising(current_row):
                # 맞으면 다음줄에 배치하러
                n_queen(current_row + 1)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())        # 체스판의 크기이자 배치할 퀸의 갯수
    answers = 0             # 정답 저장용 변수
    rows = [0] * N          # rows[idx]에 할당된 값이 idx 줄의 몇번째 칸인지를 나타내는 리스트
    n_queen(0)
    print(f'#{test_case} {answers}')
