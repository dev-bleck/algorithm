def solution(sizes):
    answer = 0
    X = Y = 0
    sizes.sort(key=lambda size: -size[0])
    for size in sizes:
        size.sort(reverse=True)
    
    for size in sizes:
        now_x, now_y = size[0], size[1]
        X = max(now_x, X)
        Y = max(now_y, Y)
        
    answer = X * Y
    return answer