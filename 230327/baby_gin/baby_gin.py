import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    counter = [0 for _ in range(10)]
    numbers = list(map(int, input()))
    for number in numbers:
        counter[number] += 1

    is_babygin = 0

    # idx를 변화시키면서 triplet 검사와 run 검사
    idx = 0
    while idx < len(counter):
        # triplet(3장이 같은 수) 검사
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        # run(3장이 연속된 3개의 숫자) 검사
        if idx < len(counter) - 2:
            # counter[idx] == 0이면 bool(counter[idx] == 0) == False (Falsy)
            if counter[idx] and counter[idx + 1] and counter[idx + 2]:
                counter[idx] -= 1
                counter[idx + 1] -= 1
                counter[idx + 2] -= 1
                is_babygin += 1
                continue
        if is_babygin == 2:
            break

        # 다음 카드 검증
        idx += 1

    if is_babygin == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
