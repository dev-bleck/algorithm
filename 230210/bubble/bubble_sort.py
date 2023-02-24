def bubble_sort(numbers):
    count = len(numbers)
    # 총 패스 수
    for i in range(count - 1):
        # 한 패스 당 비교 횟수
        for j in range(count - 1):
            # 왼쪽 > 오른쪽
            if numbers[j] > numbers[j+1]:
                # 교환
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


number_list = [2, 4, 7, 1, 3, 5, 6, 9, 8, 0]
print(bubble_sort(number_list))