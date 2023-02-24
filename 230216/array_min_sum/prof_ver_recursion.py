import sys
sys.stdin = open('sample_input.txt')

# PLAN
# selected 리스트에 각 idx에 몇번째를 선택했는지 저장한다.
# 저장이 안된 항목은 아직 선택하지 않은 것.
# 매번 DFS 마다 selected와 입력 N x N 행렬을 가지고 합을 구해보고,
# 여태까지 나온 결과 중 제일 작은 것 보다 커지면 return


def calculate_sum(arr, selected):
    temp_sum = 0
    for i in range(len(selected)):
        # selected[i]에는 i번째 줄에서 몇 번째 칸을 골랐는지 저장되어 있다
        temp_sum += arr[i][selected[i]]
    return temp_sum  # 여태 고른걸 기준으로 합하는 함수가 됨


# -------- Key Point --------
# arr : 데이터 / selected : 각 행의 몇 번째를 선택했는지
# row : 현재 찾아봐야되는 열 / size : 데이터의 크기
def test_sum(arr, selected, row, size):
    global min_sum
    temp_sum = calculate_sum(arr, selected)
    if temp_sum > min_sum:
        return
# ---------------------------

    if row == size:
        # arr에서 selected를 기반으로 현재 최소를 구하자
        temp_sum = calculate_sum(arr, selected)
        min_sum = min(min_sum, temp_sum)
        return

    # i : 0부터 size - 1까지
    for i in range(size):
        # 이미 선택한 적 있는 index이면
        if i in selected:
            # continue하고 다음 index 검사
            continue  # 아래는 실행하지 않고 for문으로 올라감
        # 이번 줄에서 선택해서 다음줄로 넘긴다
        selected.append(i)
        test_sum(arr, selected, row + 1, size)  # 다음 행에 대해서 재귀
        selected.pop()


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N

    # 각 index에는 해당하는 줄에서 선택한 index가 담긴다.
    selected = []
    row = 0  # 몇 번째 행인지 기록하기 위한 변수 row
    test_sum(arr, selected, row, N)
    print(f'#{test_case} {min_sum}')