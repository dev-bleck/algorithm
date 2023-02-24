import sys
sys.stdin = open('sample_input.txt')


# 중위 순회 : Light -> Vertex -> Right
def in_order(tree, node):
    node = int(node)
    if node != 0:
        # Left
        in_order(tree, tree[node][2])
        # Vertex
        print(f'{tree[node][1]}', end='')
        # Right
        in_order(tree, tree[node][3])

for test_case in range(1, 11):
    N = int(input())
    tree_data = [[0, 0, 0, 0]]

    for _ in range(N):
        # 정점번호, 데이터, 왼쪽, 오른쪽 input
        node_data = input().split()
        while len(node_data) != 4:
            node_data.append('0')
        tree_data.append(node_data)

    print(f'#{test_case} ', end='')
    in_order(tree_data, 1)
    print()