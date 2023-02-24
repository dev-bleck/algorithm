T = int(input())

for tc in range(1, 1 + T):
    num_lst = list(map(int, input().split()))
    N = num_lst[0]
    M = num_lst[1]
    arr = list(map(int, input().split()))

    # 리스트 안의 값을 M개씩 더해서 sum_lst 리스트에 넣기
    sum_lst = []
    for num in range(0, N - M + 1):
        sum = 0
        for idx in range(num, num + M):
            sum += arr[idx]
        sum_lst.append(sum)

    # sum_lst 순회하면서 max 값과 min 값 찾기
    max_sum = sum_lst[0]
    min_sum = sum_lst[0]
    for sum in sum_lst:
        if max_sum < sum:
            max_sum = sum
        elif min_sum > sum:
            min_sum = sum

    print(f'#{tc} {max_sum - min_sum}')