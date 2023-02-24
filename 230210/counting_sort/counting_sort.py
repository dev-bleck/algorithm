def counting_sort(numbers):
    # k = max(numbers)  # max 직접 구현해야 함
    # counts = [0] * (k + 1)  # 0부터기 때문에 k + 1까지 가야됨
    counts = [0] * 10
    number_cnt = len(numbers)

    # counts 원소 채워주기
    for i in range(number_cnt):
        counts[numbers[i]] += 1

    # counts 누적합
    for i in range(len(counts) - 1):
        # 직전 값 더하기
        counts[i + 1] += counts[i]

    result = [0] * number_cnt
    for i in range(number_cnt - 1, -1, -1):  # 뒤에서부터 정렬
        counts[numbers[i]] -= 1  # 하나 줄이고 넣어줌 10 - 1 = 9
        result[counts[numbers[i]]] = numbers[i]
    return result


# counts = [1, 1, 1, 1, 1, 1, 1, 1, 1]
number_list = [2, 4, 7, 6, 6, 5, 6, 9, 8, 0, 1, 7]
print(counting_sort(number_list))