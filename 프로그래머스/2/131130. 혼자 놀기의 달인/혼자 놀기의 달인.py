def solution(cards):
    N = len(cards)
    visited = [False] * N
    group_sizes = []

    for i in range(N):
        if not visited[i]:
            current_group_size = 0
            index = i
            
            while not visited[index]:
                visited[index] = True
                index = cards[index] - 1
                current_group_size += 1
            
            group_sizes.append(current_group_size)

    group_sizes.sort(reverse=True)

    if len(group_sizes) >= 2:
        return group_sizes[0] * group_sizes[1]
    else:
        return 0
