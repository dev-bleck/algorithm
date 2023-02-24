NMAX = 10
NMAXCANDIDATES = 10


# 남아있는 candidate를 만드는 함수이다
# a : 현재 만드는 순열 / k : 순열의 다음 칸
# input_ : 만들고자 하는 순열의 크기
# candidates : 다음에 올 후보들이 저장될 리스트
def construct_candidate(a, k, input_, candidates):
    # 순열에 사용된 적 있는지 검증
    in_perm = [False] * (NMAX + 1)

    # a를 검사하며 사용됐는지를 판단
    for i in range(1, k):
        in_perm[a[i]] = True  # 사용됐다 => True로 만들어 줌

    # n_candidates : 후보 개수 & candidates 배열의 index
    n_candidates = 0
    # 1부터 만들고자 하는 순열 크기까지 순회
    for i in range(1, input_ + 1):
        # 숫자가 사용된 적 없다
        if not in_perm[i]:
            candidates[n_candidates] = i
            n_candidates += 1

    return n_candidates


# ----- Back Tracking -----
# 실제로 순열을 만드는 함수이다
# a : 현재 만드는 순열 / k : 순열의 다음 칸
# input_ : 만들고자 하는 순열의 크기
# 결과로 만들어진 순열은 a에 저장된다
def backtrack_perm(a, k, input_):
    if k == input_:
        for i in range(1, k + 1):
            print(a[i], end=' ')
        print()
        return
    # 다음 후보를 저장할 리스트 => construct_candidates 함수에 전달할 리스트
    candidates = [0] * NMAXCANDIDATES

    k += 1

    # 다음에 올 수 있는 후보자들 수
    n_candidates = construct_candidate(a, k, input_, candidates)

    # for문을 후보자 수만큼 돌자
    for i in range(n_candidates):
        # 현재 위치에 해당 후보자 저자하고
        a[k] = candidates[i]
        # 다음 위치에 뭐 넣을지 돌리자
        backtrack_perm(a, k, input_)
# -------------------------

N = 10
a = [0] * (NMAX + 1)
backtrack_perm(a, 0, N)