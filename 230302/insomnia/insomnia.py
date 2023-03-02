import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    lst = []
    i = 0
    while len(lst) != 10:
        i += 1
        numb_list = []
        for numb in str(N * i):
            numb_list.append(numb)

        for numb in numb_list:
            if numb not in lst:
                lst.append(numb)

    print(f'#{test_case} {i * N}')
