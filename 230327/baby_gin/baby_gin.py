import sys
sys.stdin = open('sample_input.txt')


def perm(i, k):  # i: 값을 결정할 자리, k: 결정할 개수
    if i==k:
        print(*lst), card
    else:
        for j in range(1, k):  # 자신부터 오른쪽 원소들과 교환
            lst[i], lst[j] = lst[j], lst[i]
            perm(i+1, k)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())

for test_case in range(1):
    lst = [i for i in input()]
    cards = []
    perm(0, 6)
    print(f'#{test_case} {cards}')
