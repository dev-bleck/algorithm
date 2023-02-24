import sys
sys.stdin = open('sample_input.txt')


# 전위순회 : V -> L -> R
def pre_order(tree, node):
    global cnt
    if node != 0:  # 0이 아닐 때는 순회 안함
        # 나
        cnt += 1
        # 왼쪽
        pre_order(tree, tree[node][0])
        # 오른쪽
        pre_order(tree, tree[node][1])


T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    cnt = 0
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

    pre_order(tree, N)

    print(f'#{test_case} {cnt}')