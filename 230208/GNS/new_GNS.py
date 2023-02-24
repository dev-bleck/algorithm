import sys
sys.stdin = open('sample_input.txt')

T = int(input())

numb_dict = { 'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9, 'ZRO' : 0}

for test_case in range(1, T + 1):
    numb, length = input().split()
    numbs = list(map(str, input().split()))

    for i in range(int(length)):
        numbs[i] = numb_dict[numbs[i]]

    for i in range(int(length) - 1, 0, -1):
        for j in range(i):
            if numbs[j] > numbs[j+1]:
                numbs[j], numbs[j+1] = numbs[j+1], numbs[j]

    for i in range(int(length)):
        numbs[i] = list(numb_dict.keys())[numbs[i]]

    print(f'#{test_case}')
    print(*numbs)