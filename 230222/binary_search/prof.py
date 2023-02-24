import sys
sys.stdin = open('sample_input.txt')


def in_order_arr(tree, node):
    global count
    if node < len(tree):
        in_order_arr(tree, node * 2)
        tree[node] = count
        count += 1
        in_order_arr(tree, node * 2 + 1)


T = int(input())

for test_case in range(1, T + 1):
    # 노드의 개수
    N = int(input())

    tree = [[0 for _ in range(3)] for _ in range(N + 1)]

    # 완전 이진 트리는 부모자식 관계가 인덱스로 쉽게 구현됨
    for i in range(1, N + 1):
        # 내 왼쪽은 나 * 2
        tree[i][0] = 2 * i
        if 2 * i > N:
            tree[i][0] = 0
        # 내 오른쪽은 나 * 2 + 1
        tree[i][1] = 2 * i + 1
        if 2 * i + 1 > N:
            tree[i][1] = 0
        # 내 부모는 나 // 2 (사실 이 문제에선 불필요)
        tree[i][2] = i // 2

    count = 1
    # 완전 이진트리임을 알고 있으니
    # 인덱스만 가지고 풀 수 있다.
    arr_tree = [0 for _ in range(N + 1)]
    in_order_arr(arr_tree, 1)

    print(f'#{test_case} {arr_tree[1]} {arr_tree[N//2]}')
