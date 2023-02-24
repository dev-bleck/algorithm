import sys
sys.stdin = open('sample_input.txt')

# 중위 순회
def inorder(tree, node):
    global count    # 시작값
    if node <= N:   # N보다 크거나 같으면,
        inorder(tree, node * 2)        # 서브 트리의 왼쪽 자식 노드
        tree[node] = count             # 서브 트리의 루트 노드
        cnt += 1                       # 값 1 증가
        inorder(tree, node * 2 + 1)    # 서브 트리의 오른쪽 자식 노드


T = int(input())   # test case input

for test_case in range(1, T + 1):
    N = int(input())                    # N input
    tree = [0 for _ in range(N + 1)]    # 정수들을 중위 순회 순으로 저장하기 위한 리스트
    cnt = 1                             # 시작값 1
    inorder(tree, 1)                    # 함수 호출

    # tree의 루트 노드 값, N / 2번째 노드 값 출력
    # ex) tree = [0, 4, 2, 6, 1, 3, 5]
    print(f'#{test_case} {tree[1]} {tree[N // 2]}')