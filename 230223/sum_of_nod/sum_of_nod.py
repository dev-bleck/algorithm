import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # nods : 노드의 개수 / leaf_nods : 리프 노드의 개수 / target_nod : 값을 출력할 노드
    nods, leaf_nods, target_nod = map(int, input().split())

    leaf = []  # 리프 노드 번호와 값을 받을 리스트
    for _ in range(leaf_nods):
        # 리프 노드 번호와 값을 input
        leaf.append(list(map(int, input().split())))
    # ex) [[4, 1], [5, 2], [3, 3]]

    tree = [0] * (nods + 1)  # 값을 입력받을 리스트
    for i in range(len(leaf)):
        # 리프 노드에 해당 값을 입력해서 리스트로 만듬
        tree[leaf[i][0]] = leaf[i][1]
    # ex) [0, 0, 0, 3, 1, 2]

    # 아래에서 위로 진행
    # 노드의 수 - 리프 노드의 수 => 이미 채워진 노드 제외하기 위해
    for i in range(nods - leaf_nods, 0, -1):
        # 오른쪽 자식 노드가 없으면
        if i * 2 + 1 > nods:
            # 자식 노드의 값을 그대로 루트 노드로
            tree[i] = tree[i * 2]
        # 왼쪽 자식 노드와 오른쪽 자식 노드가 모두 있으면
        else:
            # 왼쪽 자식 노드의 값과 오른쪽 자식 노드의 값을 더해서 루트 노드의 값으로
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

    # 타겟 노드의 값 출력
    print(f'#{test_case} {tree[target_nod]}')
