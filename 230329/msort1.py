def msort(s, e):
    if s == e:
        return

    m = (s + e) // 2

    msort(s, m)
    msort(m + 1, e)

    # merge()
    k = 0
    l, r = s, m + 1  # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= m:
            while r <= m:
                tmp[k] = arr[m]
                m += 1
                k += 1
    i = 0
    while i < k:
        arr[s + i] = tmp[i]
        i += 1

    return


# def merge(left, right):
#     pass


# def msort(m):
    # if len(m) == 1:
    #     return m
    #
    # middle = len(m) // 2
    # left = m[0:middle]
    # right = m[middle:]

    # for x in range(left):
    #     left.append(m[x])
    #
    # for x in range(right):
    #     right.append(m[x])

    # left = msort(left)
    # right = msort(right)

    # return merge(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N  # 합치는 작업할 때 사용할 임시저장소
    msort(0, N - 1)
    print(arr)