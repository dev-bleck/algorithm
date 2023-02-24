def selection_sort(numbers):
    number_count = len(numbers)
    # 지금 넣을 위치 (i)
    for i in range(number_count - 1):
        # 비교 대상 index
        min_index = i  # 최소값의 인덱스
        # 나보다 뒤에 애들을 비교
        for j in range(i, number_count - 1):  # i가 0일 때, 0부터, 끝까지
            # 가장 작은 애가 어디 있었는지 기록
            if numbers[j + 1] < numbers[min_index]:
                min_index = j + 1
        # 가장 작은 애랑 현재(미정렬) 위치 교환
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    # 반환
    return numbers


number_list = [2, 4, 7, 6, 6, 5, 6, 9, 8, 0, 1, 7]
print(selection_sort(number_list))
