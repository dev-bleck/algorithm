# target의 부분 집합 중 합이 sum인 문제
# target : 부분 집합을 구하고 싶은 리스트
# k : 현재 추가를 결정해야 하는 원소
# n : 전체 원소의 갯수
def powerset(target, k, n):
    choose = [0, 1]

    # 마지막 원소까지 결정함
    if k == n:
        # 이번 부분 집합은 subset
        subset = []
        # 각 원소의 선택 여부 확인
        for i in range(len(choices)):
            # 각 원소를 선택했는지 확인
            if choices[i]:
                # print(target[i], end=' ')
                subset.append(target[i])

        # 총합이 10인 부분 집합은 answers에 포함시킨다
        if sum(subset) == 10:
            answers.append(subset)
    else:
        # 0은 선택 안함, 1은 선택 함
        for choice in choose:
            choices[k] = choice
            powerset(target, k + 1, n)


N = 10
target = [i for i in range(1, N + 1)]
choices = [0 for i in range(N)]  # 각 원소를 포함할지 여부에 대한 리스트
answers = []
powerset(target, 0, N)
print(answers)