# queue
list_queue = []
# enqueue => Time Complexity : O(1)
list_queue.append(10)
# 그냥 기본 pop(인자없음) => Time Complexity : 0(1)
# dequeue => Time Complexity : O(N) (N : 아이템의 개수)
list_queue.pop(0)

# 이런 상황에는 아래의 라이브러리와 클래스를 사용
from collections import deque

# 큐로 활용
deque_queue = deque()
# 큐 enqueue
deque_queue.append(11)
deque_queue.append(22)
# 큐 dequeue
print(deque_queue.popleft())  # FIFO를 위한 pop() => popleft()
print(deque_queue.popleft())  # FIFO를 위한 pop() => popleft()



# 스택으로 활용
deque_stack = deque()
# 스택 push
deque_stack.append(12)
deque_stack.append(23)
# 스택 pop
print(deque_stack.pop())  # LIFO을 위한 pop()
print(deque_stack.pop())  # LIFO을 위한 pop()
