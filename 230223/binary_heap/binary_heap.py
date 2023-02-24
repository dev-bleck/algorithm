import sys
sys.stdin = open('sample_input.txt')


def enq(node):
    heap.append(node)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbs = list(map(int, input().split()))
    heap = [0]
    for i in numbs:
        enq(i)

    lst = []
    i = len(heap) - 1
    while i != 0:
        i = i // 2
        lst.append(heap[i])

    print(f'#{test_case} {sum(lst)}')
