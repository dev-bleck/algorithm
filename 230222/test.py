'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# tree는 순회 하기 위한 tree
# node는 시작점 또는 현재점
# 재귀적으로 순회


# 전위순회 : V -> L -> R
def pre_order(tree, node):
    if node != 0:  # 0이 아닐 때는 순회 안함
        # 나
        print(f'{node}', end=' ')
        # 왼쪽
        pre_order(tree, tree[node][0])
        # 오른쪽
        pre_order(tree, tree[node][1])


# 중위순회 : L -> V -> R
def in_order(tree, node):
    if node != 0:  # 0이 아닐 때는 순회 안함
        # 왼쪽
        pre_order(tree, tree[node][0])
        # 나
        print(f'{node}', end=' ')
        # 오른쪽
        pre_order(tree, tree[node][1])


# 후위순회 : L -> R -> V
def post_order(tree, node):
    if node != 0:  # 0이 아닐 때는 순회 안함
        # 왼쪽
        pre_order(tree, tree[node][0])
        # 오른쪽
        pre_order(tree, tree[node][1])
        # 나
        print(f'{node}', end=' ')


V = int(input())  # 정점의 개수 input

# 간선의 개수는 받을 필요 없음
# 왜냐면 tree 구조 상 1개의 nod가 추가되면 1개의 간선도 추가됨
E = V - 1   # 간선 : V - 1

# l = left childs / r = right childs / p = parent
# l, r, p를 담은 리스트를 V + 1번 반복해서 생성
# 0 ~ V까지의 노드의 l, r, p 정보
# 만약 [l, r, p]의 값 중 0은 없다는 의미
tree = [[0 for _ in range(3)] for _ in range(V + 1)]

# 입력부는 문제에 따라 상이하니 주의
temp_input = list(map(int, input().split()))

for i in range(E):
    # parent, child로 입력을 구분
    parent, child = temp_input[i * 2], temp_input[i * 2 + 1]

    # 부모에게 자식 정보 업데이트
    if not tree[parent][0]:  # tree[parent][0] == 0 => 왼쪽 자식이 없다면
        tree[parent][0] = child
    # 오른쪽 자식은 무조건 없어야 됨(아니면 입력이 이상한 것)
    else:
        tree[parent][1] = child
    # 자식에게 부모 정보 업데이트
    tree[child][2] = parent

print(tree)
pre_order(tree, 1)
print()
in_order(tree, 1)
print()
post_order(tree, 1)
