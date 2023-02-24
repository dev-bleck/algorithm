'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 전위 순회
def preorder(i):
    if i:
        print(i, end=' ')
        preorder(left[i])
        preorder(right[i])

# 상동
# def preorder(i):
#     print(i, end=' ')
#     if left[i]:
#         preorder(left[i])
#     if right[i]:
#         preorder(right[i])


# 중위 순회
def inorder(i):
    if i:
        inorder(left[i])
        print(i, end=' ')
        inorder(right[i])


# 후위 순회
def postorder(i):
    if i:
        postorder(left[i])
        postorder(right[i])
        print(i, end=' ')

V = int(input())  # 노드 수
arr = list(map(int, input().split()))
E = V - 1  # 간선 수

# 부모를 인덱스로 자식번호를 저장
left = [0] * (V + 1)  # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V + 1)  # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (V + 1)  # 자식을 인덱스로 부모 저장
# child = [[] for _ in range(V + 1)]  # 이런으로 한 배열에도 저장 가능

for i in range(E):
    # p : 부모 / c : 자식
    p, c = arr[i * 2], arr[i * 2 + 1]
    if left[p] == 0:  # left의 부모 인덱스가 비어있으면
        left[p] = c  # left의 부모 인덱스에 자식 저장
    else:
        right[p] = c  # 아니면 right의 부모 인덱스에 자식 저장
    par[c] = p
    # child[p].append(c)  # 이렇게도 가능

root = 1
# 자식을 인덱스로 부모 확인 => 부모가 있으면
while par[root] != 0:  # root 찾기
    root += 1

# root부터 순회
# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)

# 5부터 순회 => 시작지가 5부터니까 루트(5)와 자식인 관계만 순회홤
preorder(5)
print()
inorder(5)
print()
postorder(5)
