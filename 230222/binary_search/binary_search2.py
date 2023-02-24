def inorder_traversal(n):
    node_list = list(range(1, n + 1))
    result = []
    def inorder(i):
        left_child = i * 2
        right_child = i * 2 + 1
        if left_child <= n:
            inorder(left_child)
        result.append(node_list[i - 1])
        if right_child <= n:
            inorder(right_child)
    inorder(1)
    return result

print(inorder_traversal(6))