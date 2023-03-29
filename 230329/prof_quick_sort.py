def quick_sort(target):
    if len(target) <= 1:
        return target
    else:
        pivot = target[0]
        left, right = [], []
        for idx in range(1, len(target)):
            if target[idx] > pivot:
                right.append(target[idx])
            elif target[idx] < pivot:
                left.append(target[idx])
    return [*quick_sort(left), pivot, *quick_sort(right)]

numbers = [11, 45, 22, 81, 33, 34, 99, 22, 17, 8]
print(quick_sort(numbers))
