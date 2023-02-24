# delta search

N, M = 10, 10
arr = [[(j, i) for i in range(M)] for j in range(N)]
# for lst in arr:
#     print(lst)

# (2, 2) 주변의 8칸을 다 검색해보기
target_i, target_j = 0, 0

# 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
directions_x = [-1, -1, -1, 0, 0, 1, 1, 1]
directions_y = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(8):
    dx = directions_x[i]
    dy = directions_y[i]
    if 0 <= target_i + dx < N and 0 <= target_j + dy < M:
        print(arr[target_i + dx][target_j + dy])