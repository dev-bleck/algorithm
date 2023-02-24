# powerset => 넣을까 말까를 생각하기
arr = list(range(1, 11))
N = len(arr)


# powerset이라는 함수의 역할
# 1. idx번째 원소를 부분집합에 포함시킬지 여부를 판단
# 2. 현재 부분집합이 유망한지(답이 될 가능성이 남아있는지) 판단
# 3. 현재 부분집합이 답인지 판단
# arr : 원소후보 / idx : idx번째 원소 / subset : 만들고 있는 원소를 담는 용도
def powerset(arr, idx, subset):
    # ----------BackTracking --------------
    # 모든 원소 확인 전 정답 검증
    if sum(subset) == 10:
        print(subset)
        return
    # 남은 것들과 현재 것들을 다 포함해도 답이 안되는 경우
    if sum(arr[idx:]) + sum(subset) < 10:
        return
    # 현재 부분집합의 합이 답이 될 가능성이 남아있는지 판단
    if sum(subset) > 10:
        return
    # -------------------------------------
    # 부분집합 다 만듬
    if idx == N:
        # 정답 검증
        if sum(subset) == 10:  # 부분집합의 합이 10면 출력
            print(subset)
        return
    # 두 갈래 상황을 확인하기 위해 재귀적으로 두번 호출해서 다음걸 확인하는 과정을 반복
    # 현재 원소 포함(왼쪽) => 현재 원소를 넣는 방향
    powerset(arr, idx + 1, subset + [arr[idx]])
    # 현재 원소 미포함(오른쪽) = > 현재 원소를 안넣는 방향
    powerset(arr, idx + 1, subset)


powerset(arr, 0, [])