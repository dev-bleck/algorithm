import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    
    max_votes = max(lst)
    max_count = lst.count(max_votes)
    
    if max_count > 1:
        print('no winner')
    else:
        if max(lst) > sum(lst) / 2:
            print(f'majority winner {lst.index(max(lst)) + 1}')
        elif max(lst) <= sum(lst) / 2:
            print(f'minority winner {lst.index(max(lst)) + 1}')