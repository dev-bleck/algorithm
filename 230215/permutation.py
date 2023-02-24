def backtrack(a, k, input_):
    c = [0] * MAXCANDIDATES

    # input이랑 k랑 동일해야 순열에 사용할 데이터를 다 고름
    if k == input_:
        for i in range(1, k + 1):
            print(a[i], end=' ')
        print()

    # 아직 다 못 고름
    else:
        k += 1
        new_candidates = construct_candidates(a, k, input_, c)
        for i in range(new_candidates):
            a[k] = c[i]
            backtrack(a, k, input_)


def construct_candidates(a, k, input_, c):
    in_perm = [False] * NMAX  # in_perm : 일종의 visited list => 이 숫자가 이미 사용되었는가
    # 해당 정보 갱신
    for i in range(1, k):
        # 쓴 적 있으면 True
        in_perm[a[i]] = True

    count = 0
    for i in range(1, input_ + 1):
        # 사용된적 없는 숫자
        if not in_perm[i]:
            c[count] = i
            count += 1

    return count


MAXCANDIDATES = 6
NMAX = 6
data = [range(10)]
a = [0] * NMAX
cnt = 0
total_cnt = 0

backtrack(a, 0, 5)


# 이렇게 하면 상당히 간단하게 가능
# 과목평가에선 X, 다른 코테에선 O
# import itertools
# data = [1, 2, 3, 4, 5]
# permutations = itertools.permutations(data, 5)
#
# for permutation in permutations:
#     print(permutation)