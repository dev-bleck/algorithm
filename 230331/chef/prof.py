import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    half = N // 2

    # 전체 식재료를 위한 집합
    all_set = {i for i in range(N)}

    synergy_graph = [list(map(int, input().split())) for _ in range(N)]

    candidates = []
    from itertools import combinations
    # combinations 함수 : 앞쪽 인자의 원소들 중 뒷쪽 인자의 갯수를 원소로 가진 부분집합으로 만들어 줌
    for combination in combinations([i for i in range(N)], half):
        candidates.append(combination)

    synergy_diff_min = sum(sum(synergy_graph, []))
    for food_a in candidates:
        # 전체 식재료 집합에서 food_a에서 사용하지 않은 식재료만 모아서 food_b로
        food_b = list(all_set.difference(set(food_a)))  # difference() : 차집합 method
        food_a_taste = 0
        food_b_taste = 0

        # half : 요리당 식재료의 갯수
        for i in range(half):
            for j in range(half):
                # food_a[i] : food_a에 사용된 i번째 식재료의 숫자
                # food_a[j] : food_a에 사용된 j번째 식재료의 숫자
                # synergy_graph[food_a[i]][food_a[j]] : food_a의 i번째 식재료와 food_a의 j번째 식재료 간의 시너지
                food_a_taste += synergy_graph[food_a[i]][food_a[j]]
                food_b_taste += synergy_graph[food_b[i]][food_b[j]]

        # 현재 만든 두 요리의 차이를 여태까지의 결과와 비교
        synergy_diff_min = min(abs(food_a_taste - food_b_taste), synergy_diff_min)

    print(f'#{test_case} {synergy_diff_min}')