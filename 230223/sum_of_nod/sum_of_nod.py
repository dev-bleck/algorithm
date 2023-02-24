import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    nods, leaf_nods, target_nod = map(int, input().split())

    leaf = []
    for _ in range(leaf_nods):
        leaf.append(list(map(int, input().split())))

    tree = [0] * (nods + 1)
    for i in range(len(leaf)):
        tree[leaf[i][0]] = leaf[i][1]

    for i in range(nods - leaf_nods, 0, -1):
        if i * 2 + 1 > nods:
            tree[i] = tree[i * 2]
        else:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

    print(f'#{test_case} {tree[target_nod]}')