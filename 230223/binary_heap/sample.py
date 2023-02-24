def enq(node):
    global last             # last = 0
    last += 1               # last = 1 => 1번 index부터
    heap[last] = node
    child = last            # 마지막으로 추가된 위치
    parent = child // 2     # 그 부모

    # 부모와 반복적으로 비교해가며 위치를 조정
    while parent > 0 and heap[parent] < heap[child]:  # parent의 index의 가장 작은 값은 1
        # heap[parent] < heap[child] : 부모가 자식보다 작으면 교체
        heap[parent], heap[child] = heap[child], heap[parent]

        # 바뀌었으면 새 부모랑 비교할 준비
        child = parent
        parent = child // 2

def deq():
    global last
    tmp = heap[1]  # root 값 저장
    heap[1] = heap[last]  # 제일 뒤에 있던 애를 제일 앞으로
    # 크기가 줄었으니 노드의 개수를 조정
    last -= 1
    parent = 1
    child = parent * 2

    while child <= last:  # 내 자식이 존재하는 동안에
        # 우측 자식도 있고, 왼쪽 자식보다 오른쪽 자식이 크다면 (이 조건은 heap의 구조를 유지하기 위함)
        if child + 1 <= last and heap[child] < heap[child + 1]:
            child += 1  # 대상을 오른쪽으로 바꾼다
        if heap[child] > heap[parent]:
            # heap을 만족시키도록 값을 교환
            heap[child], heap[parent] = heap[parent], heap[child]
            parent = child
            child = parent * 2
        # 아니면 반복 중단
        else:
            break

    return tmp


last = 0            # 힙에 추가된 총 노드들
heap = [0] * 101    # 힙 공간 확보 (0번째 index를 안쓰기 때문)

# enqueue
enq(5)
print('root :', heap[1], heap)
enq(15)
print('root :', heap[1], heap)
enq(8)
print('root :', heap[1], heap)
enq(20)
print('root :', heap[1], heap)

# dequeue
print(heap[1], heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)
print(deq(), heap)