# 최대 heap
# 최대 100개의 key
def enq(n):  # enqueue
    global last
    last += 1  # 완전이진트리에 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 저장
    c = last  # 부모가 있고, 부모 > 자식 조건 검사를 위해 방금전에 추가된걸 자식으로
    p = c // 2  # 자식 / 2의 floor 연산
    while p > 0 and heap[p] < heap[c]:  # 부모가 있고, 자식보다 부모가 작으면
        heap[p], heap[c] = heap[c], heap[p]
        c = p  # 옮긴 자리에서 부모와 비교하기 위해 부모였던 애를 자식으로
        p = c // 2  # 자식 / 2의 floor 연산
    return  # 끝

# heap에서 삭제
def deq():  # dequeue
    global last
    tmp = heap[1]           # root 임시저장(백업) 해놓기
    heap[1] = heap[last]    # 마지막 노드 제거하고 그 값을 root로
    last -= 1               # 마지막 정점 삭제
    p = 1                   # root를 부모로 놓고
    c = p * 2               # 왼쪽 자식 번호
    while c <= last:        # 자식이 하나 이상 있는가? (없으면 끝)
        if c + 1 <= last and heap[c] < heap[c + 1]:   # 오른쪽 자식도 있고, 오른쪽 자식이 왼쪽 자식보다 크
            c += 1          # 비교 대상을 오른쪽 자식으로 변경한다
        if heap[c] > heap[p]:  # 자식의 key 값이 부모의 key 값보다 크다면,
            heap[c], heap[p] = heap[p], heap[c]  # 교환
            p = c
            c = p * 2
        else:
            break           # 탈출
    return tmp


heap = [0] * 101  # 완전이진트리 : 1번 ~ 100번 인덱스 준비
last = 0  # 완전이진트리의 마지막 정점 번호 초기화
enq(5)
print(heap[1])  # root : 5 (5가 제일 큼)
enq(15)
print(heap[1])  # root : 15 (15가 제일 큼)
enq(8)
print(heap[1])  # root : 15 (15가 제일 큼)
enq(20)
print(heap[1], heap)  # root : 20 (20이 제일 큼)

while last > 1:
    print(deq())  # 큰 순서대로 출력